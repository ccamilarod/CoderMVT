from django.db import models

# Create your models here.

class Familia(models.Model):

    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    birth = models.CharField(max_length=100)