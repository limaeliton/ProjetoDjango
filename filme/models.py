from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

LISTA_CATEGORIAS = (
    ("ANALISES" , "Análises"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros"),
)

# criar o filme
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

# python manage.py makemigrations, python manage.py migrate quando criar uma tabela no banco tem que roda esses comandos.

# criar os episódios
class Episodio(models.Model):
# chave extrangeira ser sempre o primeiro campo , related_name cria os episódios
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
# é um link
    video = models.URLField()


    def __str__(self):
        return self.filme.titulo + " - " + self.titulo


class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme")

# tem que adicionar no admin.py
# quando criar um classe no Models é necessário rodar os
# comandos python manage.py makemigrations, python manage.py migrate quando criar uma tabela no banco tem que roda esses comandos.
