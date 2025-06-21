from django.db import models

# Create your models here.

class Exam(models.Model):
    """
    Modelo para representar um Exame.
    """

    exam_name = models.CharField(
        max_length=100,
        verbose_name="Exame",
        unique=True 
    )
    # TODO: Mudar para preechimento obrigatório.
    description = models.TextField(
        verbose_name="Descrição",
        null=True,
        blank=True,
        max_length=1200,
    )
    # TODO: Mudar para preechimento obrigatório.
    preparation = models.TextField(
        verbose_name="Preparação",
        null=True,
        blank=True,
        max_length=1200
    )

    class Meta:
        verbose_name = "Exame"
        verbose_name_plural = "Exames"
        ordering = ['exam_name']

    def __str__(self):
        """
        Representação textual do objeto Exam.
        """
        return self.exam_name