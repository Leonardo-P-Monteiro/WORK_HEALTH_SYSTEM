# DJANGO IMPORTS 
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.text import slugify
from django.core.exceptions import ValidationError

# MY IMPORTS
from exam import models as exam
from safety import models as safety
from training import models as training
from gemini.client import iagen

# Create your models here.

# INTERMEDIARY MODELS TO FUNCTION

class FunctionRiskPhysical(models.Model):
    function = models.ForeignKey(
        'Function',
        on_delete= models.CASCADE,
        related_name= 'applied_risks_physical'
    )
    risk_physical = models.ForeignKey(
        safety.RiskPhysical,
        on_delete= models.PROTECT,
        verbose_name= 'Risco Físico'
    )
    expositions = models.ManyToManyField(
        safety.ExpositionRisk,
        verbose_name= 'Tipo de Exposição'
    )

    class Meta:
        verbose_name = 'Risco Físico Aplicado à Função'
        verbose_name_plural = 'Riscos Físicos Aplicados à Função'
        unique_together = ('function', 'risk_physical')

    def __str__(self):
        return f"Risco Físico Aplicado: {self.risk_physical.name} para {self.function.name}"

class FunctionRiskErgonomic(models.Model):
    function = models.ForeignKey(
        'Function',
        on_delete= models.CASCADE,
        related_name= 'applied_risks_ergonomic'
    )
    risk_ergonomic = models.ForeignKey(
        safety.RiskErgonomic,
        on_delete= models.PROTECT,
        verbose_name= 'Risco Ergonômico'
    )
    expositions = models.ManyToManyField(
        safety.ExpositionRisk,
        verbose_name= 'Tipo de Exposição'
    )

    class Meta:
        verbose_name = 'Risco Ergonômico Aplicado à Função'
        verbose_name_plural = 'Riscos Ergonômicos Aplicados à Função'
        unique_together = ('function', 'risk_ergonomic')

    def __str__(self):
        return f"Risco Ergonômico Aplicado: {self.risk_ergonomic.name} para {self.function.name}"

class FunctionRiskBiological(models.Model):
    function = models.ForeignKey(
        'Function',
        on_delete= models.CASCADE,
        related_name= 'applied_risks_biological'
    )
    risk_biological = models.ForeignKey(
        safety.RiskBiological,
        on_delete= models.PROTECT,
        verbose_name= 'Risco Biológico'
    )
    expositions = models.ManyToManyField(
        safety.ExpositionRisk,
        verbose_name= 'Tipo de Exposição'
    )

    class Meta:
        verbose_name = 'Risco Biológico Ergonômico Aplicado à Função'
        verbose_name_plural = 'Riscos Biológicos Aplicados à Função'
        unique_together = ('function', 'risk_biological')

    def __str__(self):
        return f"Risco Físico Aplicado: {self.risk_biological.name} para {self.function.name}"

class FunctionRiskAccident(models.Model):
    function = models.ForeignKey(
        'Function',
        on_delete= models.CASCADE,
        related_name= 'applied_risks_accident'
    )
    risk_accident = models.ForeignKey(
        safety.RiskAccident,
        on_delete= models.PROTECT,
        verbose_name= 'Risco de Acidente'
    )
    expositions = models.ManyToManyField(
        safety.ExpositionRisk,
        verbose_name= 'Tipo de Exposição'
    )

    class Meta:
        verbose_name = 'Risco de Acidente Aplicado à Função'
        verbose_name_plural = 'Riscos de Acidentes Aplicados à Função'
        unique_together = ('function', 'risk_accident')

    def __str__(self):
        return f"Risco de Acidente Aplicado: {self.risk_accident.name} para {self.function.name}"

class FunctionRiskChemical(models.Model):
    function = models.ForeignKey(
        'Function',
        on_delete= models.CASCADE,
        related_name= 'applied_risks_chemical'
    )
    risk_chemical = models.ForeignKey(
        safety.RiskChemical,
        on_delete= models.PROTECT,
        verbose_name= 'Risco Químico'
    )
    expositions = models.ManyToManyField(
        safety.ExpositionRisk,
        verbose_name= 'Tipo de Exposição'
    )

    class Meta:
        verbose_name = 'Risco Químico Aplicado à Função'
        verbose_name_plural = 'Riscos Químicos Aplicados à Função'
        unique_together = ('function', 'risk_chemical')

    def __str__(self):
        return f"Risco Químico Aplicado: {self.risk_chemical.name} para {self.function.name}"

# INTERMEDIARY MODELS TO FUNCTION

class SpecialActivityRiskPhysical(models.Model):
    special_activity = models.ForeignKey(
        'SpecialActivity',
        on_delete= models.CASCADE,
        related_name= 'applied_risks_physical'
    )
    risk_physical = models.ForeignKey(
        safety.RiskPhysical,
        on_delete= models.PROTECT,
        verbose_name= 'Risco Físico'
    )
    expositions = models.ManyToManyField(
        safety.ExpositionRisk,
        verbose_name= 'Tipo de Exposição'
    )

    class Meta:
        verbose_name = 'Risco Físico Aplicado à Atividade Especial'
        verbose_name_plural = 'Riscos Físicos Aplicados à Atividade Especial'
        unique_together = ('special_activity', 'risk_physical')
    
    def __str__(self):
        selected_exp = ', '.join((e.name for e in self.expositions.all()))
        return f'{self.risk_physical.name} para {self.special_activity.name}. \
            Exposições: {selected_exp or 'Nenhuma'}.'

class SpecialActivityErgonomic(models.Model):
    special_activity = models.ForeignKey(
        'SpecialActivity',
        on_delete= models.CASCADE,
        related_name= 'applied_risks_ergonomic'
    )
    risk_ergonomic = models.ForeignKey(
        safety.RiskErgonomic,
        on_delete= models.PROTECT,
        verbose_name= 'Risco Ergonômico'
    )
    expositions = models.ManyToManyField(
        safety.ExpositionRisk,
        verbose_name= 'Tipo de Exposição'
    )

    class Meta:
        verbose_name = 'Risco Ergonômico Aplicado à Atividade Especial'
        verbose_name_plural = 'Riscos Ergonômicos Aplicados à Atividade Especial'
        unique_together = ('special_activity', 'risk_ergonomic')
    
    def __str__(self):
        selected_exp = ', '.join((e.name for e in self.expositions.all()))
        return f'{self.risk_ergonomic.name} para {self.special_activity.name}. \
            Exposições: {selected_exp or 'Nenhuma'}.'

class SpecialActivityBiological(models.Model):
    special_activity = models.ForeignKey(
        'SpecialActivity',
        on_delete= models.CASCADE,
        related_name= 'applied_risks_biological'
    )
    risk_biological = models.ForeignKey(
        safety.RiskBiological,
        on_delete= models.PROTECT,
        verbose_name= 'Risco Biológico'
    )
    expositions = models.ManyToManyField(
        safety.ExpositionRisk,
        verbose_name= 'Tipo de Exposição'
    )

    class Meta:
        verbose_name = 'Risco Biológico Aplicado à Atividade Especial'
        verbose_name_plural = 'Riscos Biológicos Aplicados à Atividade Especial'
        unique_together = ('special_activity', 'risk_biological')
    
    def __str__(self):
        selected_exp = ', '.join((e.name for e in self.expositions.all()))
        return f'{self.risk_biological.name} para {self.special_activity.name}. \
            Exposições: {selected_exp or 'Nenhuma'}.'

class SpecialActivityAccident(models.Model):
    special_activity = models.ForeignKey(
        'SpecialActivity',
        on_delete= models.CASCADE,
        related_name= 'applied_risks_accident'
    )
    risk_accident = models.ForeignKey(
        safety.RiskAccident,
        on_delete= models.PROTECT,
        verbose_name= 'Risco de Acidente'
    )
    expositions = models.ManyToManyField(
        safety.ExpositionRisk,
        verbose_name= 'Tipo de Exposição'
    )

    class Meta:
        verbose_name = 'Risco de Acidente Aplicado à Atividade Especial'
        verbose_name_plural = 'Riscos de Acidentes Aplicados à Atividade Especial'
        unique_together = ('special_activity', 'risk_accident')
    
    def __str__(self):
        selected_exp = ', '.join((e.name for e in self.expositions.all()))
        return f'{self.risk_accident.name} para {self.special_activity.name}. \
            Exposições: {selected_exp or 'Nenhuma'}.'

class SpecialActivityChemical(models.Model):
    special_activity = models.ForeignKey(
        'SpecialActivity',
        on_delete= models.CASCADE,
        related_name= 'applied_risks_chemical'
    )
    risk_chemical = models.ForeignKey(
        safety.RiskChemical,
        on_delete= models.PROTECT,
        verbose_name= 'Risco Químico'
    )
    expositions = models.ManyToManyField(
        safety.ExpositionRisk,
        verbose_name= 'Tipo de Exposição'
    )

    class Meta:
        verbose_name = 'Risco Químico Aplicado à Atividade Especial'
        verbose_name_plural = 'Riscos Químicos Aplicados à Atividade Especial'
        unique_together = ('special_activity', 'risk_chemical')
    
    def __str__(self):
        selected_exp = ', '.join((e.name for e in self.expositions.all()))
        return f'{self.risk_chemical.name} para {self.special_activity.name}. \
            Exposições: {selected_exp or 'Nenhuma'}.'

# PRINCPAL MODELS

class SpecialActivity(models.Model):
    """
    Modelo para representar uma Atividade Especial e seus requisitos associados.
    """
    # Opções para o campo 'mandatory_epi'
    MANDATORY_CHOICES = [
        ('OBRIGATORIO EM ATIVIDADES ESPECIFICAS',
            'Obrigatório em atividades específicas'),
        ('OBRIGATORIO EM TODAS AS ATIVIDADES', 
            'Obrigatório em todas as atividades'),
        ('OBRIGATORIO AO CIRCULAR PELA AREA DE PRODUCAO', 
            'Obrigatório ao circular pela área de produção'),
        ('RECOMENDADO', 'Recomendado')
    ]

    name = models.CharField(
        max_length=100,
        verbose_name= "Nome da Atividade Especial"
    )

    description = models.TextField(
        max_length= 6000,
        verbose_name= "Descrição",
        null=True,
        blank=True
    )

    trainings = models.ManyToManyField(
        training.Training,
        verbose_name= "Treinamentos Requeridos",
        blank=True
    )

    epis = models.ManyToManyField(
        safety.Epi, 
        verbose_name= "EPIs Necessários",
        blank=True
    )

    mandatory = models.CharField(
        max_length= 45,
        choices=MANDATORY_CHOICES,
        verbose_name= "Obrigatoriedade",
        help_text= 'Esse campo diz respeito se o EPI é \
                    recomendado ou obrigatório.',
        null=True,
        blank=True
    )

    exams_admissional = models.ManyToManyField(
        exam.Exam,
        verbose_name= "Exames Admissionais",
        blank=True,
        related_name= 'sa_exams_admissional'
    )

    exams_periodic = models.ManyToManyField(
        exam.Exam,
        verbose_name= "Exames Periódicos",
        blank=True,
        related_name='sa_exams_periodic'
    )

    exams_dismissal = models.ManyToManyField(
        exam.Exam,
        verbose_name= "Exames Demissionais",
        blank=True,
        related_name= 'sa_exams_dismissal'
    )

    exams_return_work = models.ManyToManyField(
        exam.Exam,
        verbose_name= "Exames de Retorno ao Trabalho",
        blank=True,
        related_name= 'sa_exams_return_work'
    )

    exams_change_function = models.ManyToManyField(
        exam.Exam,
        verbose_name= "Exames de Mudança de Função",
        blank=True,
        related_name= 'sa_exams_change_function'
    )

    slug = models.SlugField(unique=True, null=True, max_length=140, editable=False )

    class Meta:
        verbose_name = "Atividade Especial"
        verbose_name_plural = "Atividades Especiais"
        ordering = ['name']

    #TODO: Aqui vai ser preciso criar um template exclusivo pra exibição delas.
    def get_absolute_url(self):
        return reverse('function:details', args=[self.slug])

    def clean(self):
        new_slug = slugify(self.name)
        
        # Verifica se o slug já existe (excluindo o objeto atual se for uma atualização)
        if SpecialActivity.objects.exclude(pk=self.pk).filter(slug=new_slug).exists():
            raise ValidationError(f"Já existe uma função com o slug '{new_slug}'. Por favor, altere o nome.")
        
        self.slug = new_slug

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Function(models.Model):
    """
    Modelo para representar uma Função/Cargo na organização.
    """

    MANDATORY_CHOICES = [
        ('OBRIGATORIO EM ATIVIDADES ESPECIFICAS',
        'Obrigatório em atividades específicas'),

        ('OBRIGATORIO EM TODAS AS ATIVIDADES', 
        'Obrigatório em todas as atividades'),

        ('OBRIGATORIO AO CIRCULAR PELA AREA DE PRODUCAO', 
        'Obrigatório ao circular pela área de produção'),

        ('RECOMENDADO', 'Recomendado')
    ]

    name = models.CharField(
        max_length=100,
        verbose_name= "Nome da Função"
    )

    description = models.TextField(
        verbose_name= "Descrição da Função",
        null=True,
        blank=True,
        max_length= 6000,
    )

    cbo = models.CharField(
        max_length=15,
        verbose_name= "CBO",
        null=True,
        blank=True
    )

    special_activities = models.ManyToManyField(
        SpecialActivity,
        related_name='functions',
        verbose_name= "Atividades Especiais Associadas",
        blank=True
    )

    trainings = models.ManyToManyField(
        training.Training,
        related_name='functions',
        verbose_name= "Treinamentos Requeridos pela Função",
        blank=True
    )

    epis = models.ManyToManyField(
        safety.Epi,
        related_name='functions',
        verbose_name="EPIs Associados à Função",
        blank=True,
    )

    epi_mandatory = models.CharField(
        max_length= 45,
        choices=MANDATORY_CHOICES,
        verbose_name= "Obrigatoriedade de EPI",
        help_text= "Define a regra geral de obrigatoriedade de EPI para esta função.",
        null=True,
        blank=True,
    )

    exams_admissional = models.ManyToManyField(
        exam.Exam,
        related_name='function_exams_admissional', 
        verbose_name= "Exames Admissionais",
        blank=True,
    )

    exams_periodic = models.ManyToManyField(
        exam.Exam,
        verbose_name= "Exames Periódicos",
        related_name='function_exams_periodic',
        blank=True
    )

    exams_dismissal = models.ManyToManyField(
        exam.Exam,
        related_name='function_exams_dismissal',
        verbose_name= "Exames Demissionais",
        blank=True
    )

    exams_return_work = models.ManyToManyField(
        exam.Exam,
        related_name='function_exams_return_work',
        verbose_name= "Exames de Retorno ao Trabalho",
        blank=True
    )

    exams_change_function = models.ManyToManyField(
        'exam.Exam',
        related_name='function_exams_change_function',
        verbose_name= "Exames de Mudança de Função",
        blank=True
    )

    slug = models.SlugField(unique=True, null=True, max_length=140, editable=False )

    class Meta:
        verbose_name = "Função"
        verbose_name_plural = "Funções"
        ordering = ['name']


    def clean(self):
        if self.cbo:
            new_slug = slugify(f"{self.name} {self.cbo}")
        else:
            new_slug = slugify(self.name)
        
        # Verifica se o slug já existe (excluindo o objeto atual se for uma atualização)
        if Function.objects.exclude(pk=self.pk).filter(slug=new_slug).exists():
            raise ValidationError(f"Já existe uma função com o slug '{new_slug}'. Por favor, altere o nome ou CBO.")
        
        self.slug = new_slug

        if not self.description:
            self.description = iagen(function=self.name, cbo=self.cbo)

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
        

    def get_absolute_url(self):
        return reverse('function:details', args=[self.slug])

    def __str__(self):
        return self.name
