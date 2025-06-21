# DJANGO IMPORTS
from django.contrib import admin
from django.urls import path
# MY IMPORTS 
from .views import login, logout, search, HomeListView, DetailsView, \
    details_report, FunctionCompendiumView # Importe a nova view aqui


app_name = 'function'

urlpatterns = [
    path('', login, name='login'), #type:ignore
    path('logout/', logout, name='logout'),
    path('home/', HomeListView.as_view(), name='home'),
    path('details/<slug:function>/', DetailsView.as_view(), name='details'),
    path(
        'report/<slug:function_slug>/', details_report, name='report'),
    path('search/', search, name='search'),
    # Nova URL para o compêndio de funções
    # A view FunctionCompendiumView é usada aqui.
    path('compendium/', FunctionCompendiumView.as_view(), name='compendium'),
]