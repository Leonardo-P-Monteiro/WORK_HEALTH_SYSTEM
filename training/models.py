from django.db import models

# Create your models here.

class Training(models.Model):
    """
    Modelo para representar um Treinamento.
    """
    # Opções para o campo 'mandatory'
    MANDATORY_CHOICES = [
        ('RECOMENDADO','Recomendado'),
        ('OBRIGATORIO','Obrigatório'),
    ]

    # CAMPOS DO MODELO
    name = models.CharField(
        max_length=100,
        verbose_name= "Treinamento",
        unique=True 
    )

    # TODO: Mudar para preechimento obrigatório.
    description = models.TextField(
        verbose_name= "Descrição",
        null=True,
        blank=True,
        max_length=1200
    )
# Suspendido por não ser pertinente aqui.
    # mandatory = models.CharField(
    #     max_length=20,
    #     choices=MANDATORY_CHOICES,
    #     verbose_name="Obrigatoriedade",
    #     null=True,
    #     blank=True,
    # )

    class Meta:
        verbose_name = "Treinamento"
        verbose_name_plural = "Treinamentos"
        ordering = ['name'] # Opcional: ordena por nome

    def __str__(self):
        """
        Representação textual do objeto Training.
        """
        return self.name