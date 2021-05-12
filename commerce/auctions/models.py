from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class categ(models.Model):
    cat = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.id}: {self.cat}"

class leilao(models.Model):
    titulo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=10)
    valor_min = models.IntegerField()
    foto = models.ImageField()
    categ = models.ForeignKey(categ,on_delete=models.CASCADE, related_name="cat")
 
    def __str__(self):
        return f"{self.id}: {self.titulo} | {self.descricao} | {self.valor_min} | {self.foto} | {self.categ}"
