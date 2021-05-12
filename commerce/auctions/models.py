from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image


class User(AbstractUser):
    pass

class categ(models.Model):
    cat = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.id}: {self.cat}"

class leilao(models.Model):
    titulo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=10)
    valor_min = models.IntegerField()
    foto = models.ImageField(upload_to='fotos/')
    categ = models.ForeignKey(categ,on_delete=models.CASCADE, related_name="categorias")
 
    def __str__(self):
        return f"{self.id}: {self.titulo} | {self.descricao} | {self.valor_min} | {self.foto.url} | {self.categ}"