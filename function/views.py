# DJANGO IMPORTS
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Remova a importação de Paginator se não for mais usada em outras partes da view,
# ou a mantenha se houver outras views paginadas.
from django.core.paginator import Paginator 

# MY IMPORTS
from django.views.generic import ListView, DetailView, View
from function.models import Function, SpecialActivity # Importação da classe Function e SpecialActivity
from utils.functions import get_combined_fields
from django.contrib import messages, auth



# Create your views here.

def login(request):
    form = AuthenticationForm()

    if request.user.is_authenticated:
        return redirect('function:home')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('function:home')
        
        else:
            return render(request, 'function/login.html', {'error_message':'Usuário ou senha incorreto.'})


    else:
        return render(request, 'function/login.html', {'form':form})

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return render(request, 'function/login.html', {'success_message':'Logout feito com sucesso.'})

    return render(request, 'function/login.html')

@method_decorator(login_required(login_url='function:login'), name='dispatch')
class HomeListView(ListView): 
    model = Function
    queryset = Function.objects.all().order_by('name')
    template_name = 'function/home.html'
    context_object_name = 'object_list'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona 'is_first_load' para a HomeListView
        context['is_first_load'] = True 
        return context

@method_decorator(login_required(login_url='function:login'), name='dispatch')
class DetailsView(DetailView):
    model = Function
    template_name = 'function/details.html'
    context_object_name = 'function'
    slug_url_kwarg = 'function'

# Nova View para o Compêndio de Funções (SEM PAGINAÇÃO)
@method_decorator(login_required(login_url='function:login'), name='dispatch')
class FunctionCompendiumView(ListView):
    model = Function # Define o modelo a ser listado como Function
    template_name = 'function/compendium.html' # Novo template para o compêndio
    context_object_name = 'functions' # Nome da variável que conterá a lista de funções no template

    def get_queryset(self):
        # Otimiza a busca carregando todos os relacionamentos de uma vez
        # para evitar múltiplos acessos ao banco de dados (problema N+1).
        # Não há paginação, então retornamos todos os objetos.
        queryset = Function.objects.prefetch_related(
            'applied_risks_chemical', 'applied_risks_physical', 'applied_risks_biological', 
            'applied_risks_accident', 'applied_risks_ergonomic', 'trainings', 'epis',
            'exams_admissional', 'exams_periodic', 'exams_dismissal', 
            'exams_return_work', 'exams_change_function', 'special_activities'
        ).order_by('name') # Ordena as funções pelo nome
        return queryset

    # Não precisamos de get_context_data específico para paginação aqui,
    # pois a intenção é não ter paginação.

# TODO: Precisamos inserir aqui nos resultados das buscas as atividades especiais.
@login_required(login_url='function:login')
def search(request):
    
    qp = request.GET.get('q','')

    is_first_load = not bool(qp) # Se 'qp' estiver vazio, é a primeira carga ou uma busca vazia.

    if qp:
        qs = Function.objects.filter(
            Q(name__icontains=qp)|
            Q(description__icontains=qp)|
            Q(cbo__icontains=qp)|
            Q(special_activities__name__icontains=qp)
        ).distinct().order_by('name')
    else:
        qs = Function.objects.all().order_by('name') # Isso pode ser otimizado para não buscar tudo se for is_first_load e não tiver qs

    # PAGINATION
    is_paginated = True
    numb_pages = 12
    paginator = Paginator(qs, numb_pages)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'q': qp,
        'page_obj': page_obj,
        'is_paginated': is_paginated,
        'is_first_load': is_first_load and not qp, # Garante que só seja True se 'qp' for vazio
        'has_results': bool(page_obj) # Verifica se há resultados na busca
    }

    return render(request, 'function/home.html', context)

@login_required(login_url='function:login')
def details_report(request, function_slug):
    function = Function.objects.prefetch_related(
        'applied_risks_chemical', 'applied_risks_physical', 'applied_risks_biological', 
        'applied_risks_accident', 'applied_risks_ergonomic', 'trainings', 'epis',
        'exams_admissional', 'exams_periodic', 'exams_dismissal', 
        'exams_return_work', 'exams_change_function'
    ).get(slug=function_slug)
    
    # Lista das atividades especiais disponíveis para esta função
    available_activities = SpecialActivity.objects.filter(
        functions=function
    ).prefetch_related(
        'applied_risks_chemical', 'applied_risks_physical', 'applied_risks_biological', 
        'applied_risks_accident', 'applied_risks_ergonomic', 'trainings', 'epis',
        'exams_admissional', 'exams_periodic', 'exams_dismissal', 
        'exams_return_work', 'exams_change_function'
    )
    
    # Para processar o formulário quando enviado
    if request.method == 'POST':
        # Pega os IDs das atividades especiais selecionadas
        selected_activity_ids = request.POST.getlist('special_activities')
        print('>>>>>>>>>>>>>>>>>' ,selected_activity_ids)
        
        # Filtra as atividades selecionadas
        selected_activities = [
            activity for activity in available_activities 
            if str(activity.id) in selected_activity_ids #type: ignore
        ]
        
        # Obtém todos os campos combinados
        combined_fields = get_combined_fields(function, selected_activities)
        
        context = {
            'function': function,
            'available_activities': available_activities,
            'selected_activities': selected_activities,
            'combined_fields': combined_fields,
        }
        
        return render(request, 'function/details_report.html', context)
    
    # Para o GET inicial.
    return redirect('function:home')


    def get(self, request, *args, **kwargs):
        # 1. Obter os dados das funções, como na FunctionCompendiumView.
        functions = Function.objects.prefetch_related(
            'applied_risks_chemical', 'applied_risks_physical', 'applied_risks_biological', 
            'applied_risks_accident', 'applied_risks_ergonomic', 'trainings', 'epis',
            'exams_admissional', 'exams_periodic', 'exams_dismissal', 
            'exams_return_work', 'exams_change_function', 'special_activities'
        ).order_by('name')

        # 2. Preparar o contexto para o template.
        context = {
            'functions': functions,
            'request': request, # Passa o request para o template, útil para {% static %}
            'is_pdf': True,     # Indica que é uma renderização para PDF (pode ser usado para esconder botões etc.)
        }
        
        # 3. Chamar a função utilitária para gerar o PDF.
        pdf_response = render_to_pdf_utility('function/compendium.html', context)

        # 4. Retornar a resposta HTTP.
        if pdf_response:
            # Define o cabeçalho Content-Disposition para que o navegador baixe o arquivo.
            pdf_response['Content-Disposition'] = 'attachment; filename="compendio_funcoes.pdf"'
            return pdf_response
        
        # Se a geração do PDF falhar, retorna uma mensagem de erro.
        return HttpResponse("Desculpe, algo deu errado ao gerar o PDF.", status=500)