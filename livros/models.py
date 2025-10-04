from django.db import models

# Create your models here.
class Livro (models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    data_public = models.DateField(auto_now=False, auto_now_add=False)
    descricao = models.CharField(max_length=9000)
    disponivel = True

    def __str__(self):
        return Livro.titulo