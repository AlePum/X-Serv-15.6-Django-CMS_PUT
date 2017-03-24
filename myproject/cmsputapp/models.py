from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pelicula(models.Model):
    Titulo = models.CharField(max_length=64)
    TitOrig = models.CharField(max_length=64)
    TresD = models.BooleanFiel(Default = True)

class Proyeccion(models.Model):
    Hora = models.DateTimeField()
    Precio = models.FloatField()
    Sala = models.PositiveIntegerField()
    Pelicula = models.ForeignKey(Pelicula)
