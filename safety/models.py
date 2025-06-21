# DJANGO IMPORTS 
from django.db import models

# MY IMPORTS

# Create your models here.

class ExpositionRisk(models.Model):
    """
    Modelo para representar o Tipo ou Forma de Exposição ao Risco.
    """
    name = models.CharField(
        max_length=100,
        verbose_name= "Exposição",
        unique=True
    )

    description = models.TextField(
        verbose_name="Descrição",
        max_length=1200,
        blank= True,
        null= True,
    )

    class Meta:
        verbose_name = "Tipo de Exposição"
        verbose_name_plural = "Tipos de Exposição"
        ordering = ['name']

    def __str__(self):
        return self.name

class RiskChemical(models.Model):
    """
    Modelo para representar um Risco Químico.
    """
    name = models.CharField(
        max_length=100,
        verbose_name= "Nome do Risco",
        unique=True,
    )

    description = models.TextField(
        verbose_name= "Descrição",
        blank= True,
        null= True,
        max_length= 1200,
    )

    type_risk_chemical = models.TextField(
        verbose_name= 'Tipo de Risco Químico',
        blank=True,
        null=True,
        max_length= 120,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Risco Químico"
        verbose_name_plural = "Riscos Químicos"
        ordering = ['name']

class RiskPhysical(models.Model):
    """
    Modelo para representar um Risco Físico.
    """
    name = models.CharField(
        max_length=100,
        verbose_name= "Nome do Risco",
        unique=True,
    )

    description = models.TextField(
        verbose_name= "Descrição",
        blank= True,
        null= True,
        max_length= 1200,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Risco Físico"
        verbose_name_plural = "Riscos Físicos"
        ordering = ['name']

class RiskBiological(models.Model):
    """
    Modelo para representar um Risco Biológico.
    """
    name = models.CharField(
        max_length=100,
        verbose_name= "Nome do Risco",
        unique=True,
    )

    description = models.TextField(
        verbose_name= "Descrição",
        blank= True,
        null= True,
        max_length= 1200,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Risco Biológico"
        verbose_name_plural = "Riscos Biológicos"
        ordering = ['name']

class RiskAccident(models.Model):
    """
    Modelo para representar um Risco de Acidente.
    """
    name = models.CharField(
        max_length=100,
        verbose_name= "Nome do Risco",
        unique=True,
    )

    description = models.TextField(
        verbose_name= "Descrição",
        blank= True,
        null= True,
        max_length= 1200,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Risco de Acidente"
        verbose_name_plural = "Riscos de Acidentes"
        ordering = ['name']

class RiskErgonomic(models.Model):
    """
    Modelo para representar um Risco Ergonômico.
    """
    name = models.CharField(
        max_length=100,
        verbose_name= "Nome do Risco",
        unique=True,
    )

    description = models.TextField(
        verbose_name= "Descrição",
        blank= True,
        null= True,
        max_length= 1200,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Risco Ergonômico"
        verbose_name_plural = "Riscos Ergonômicos"
        ordering = ['name']

class TypeEpi(models.Model):
    """
    Modelo para representar os Tipos de Equipamento de Proteção Individual (EPI).
    """

    name = models.CharField(
        max_length=100, 
        verbose_name= "Tipo de EPI",
        unique=True 
    )

    description = models.TextField(
        verbose_name= "Descrição",
        null=True,
        blank=True,
        max_length= 1200,
    )

    class Meta:
        verbose_name = "Tipo de EPI"
        verbose_name_plural = "Tipos de EPI"
        ordering = ['name']

    def __str__(self):
        return self.name

class Epi(models.Model):
    """
    Modelo para representar um Equipamento de Proteção Individual (EPI) 
    específico.
    """

    # TODO: Remova se o campo já não for mais pertinente.
    # Essas opções foram removidas por conta do campo mandatory não precisar estar aqui.
    # Opções para o campo 'mandatory'
    # MANDATORY_CHOICES = [
    #     ('OBRIGATORIO EM ATIVIDADES ESPECIFICAS',
    #         'Obrigatório em atividades específicas'),
    #     ('OBRIGATORIO EM TODAS AS ATIVIDADES', 
    #         'Obrigatório em todas as atividades'),
    #     ('OBRIGATORIO AO CIRCULAR PELA AREA DE PRODUCAO', 
    #         'Obrigatório ao circular pela área de produção'),
    #     ('RECOMENDADO', 'Recomendado')
    # ]

    name = models.CharField(
        max_length=100,
        verbose_name= "EPI"
    )

    description = models.TextField(
        verbose_name= "Descrição",
        null=True,
        blank=True,
        max_length= 1200,
    )

    #TODO: Avalie se aqui realmente precisa ser N:N. Pois cada EPI, em 
    # meu entendimento, deveria estar em apenas um tipo/categoria de EPI.
    # Vou mudar para ForeignKey para cada EPI ter vínculo com apenas um tipo.
    type_epi = models.ForeignKey(
        TypeEpi,
        verbose_name= "Tipo de EPI",
        blank=False,
        null= False,
        on_delete= models.PROTECT,
    )

# O campo "mandatory" foi removido pois ele vai estar incluído na tabela 
# de functions.
    # mandatory = models.CharField(
    #     max_length=50,
    #     choices=MANDATORY_CHOICES,
    #     verbose_name= "Obrigatoriedade",
    #     help_text= 'Esse campo diz respeito se o EPI é 
    # recomendado ou obrigatório.',
    #     null=True,
    #     blank=True
    # )

    class Meta:
        verbose_name = "EPI"
        verbose_name_plural = "EPIs"
        ordering = ['name']

    def __str__(self):
        return self.name
