from ast import ClassDef
import email
from statistics import quantiles
from unittest.util import _MAX_LENGTH
from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)
     
    def __str__(self):
        return self.descricao

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField()

    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.Charfield(max_length=100)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=32)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey()
