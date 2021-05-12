from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Flight(models.Model):
    origin = models.ForeignKey(max_length=10)
    destination = models.ForeignKey(max_length=10)
    duration = models.IntegerField()
 
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
