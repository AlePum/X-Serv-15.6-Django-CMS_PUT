from django.shortcuts import render
from django.http import HttpResponse
from models import Pelicula

# Create your views here.

def Pelicula(request, identificador):

    try:
        identificador = int(identificador)
    except ValueError
        respuesta = "El identificador ha de ser un entero"
    try:
        peli = Pelicula.objects.get(id = identificador)
        respuesta = "Tu pelicula es " + peli.Titulo
    except Pelicula.DoesNotExist
        respuesta = "No existe esa pelicula"
    return HttpResponse(respuesta)

def nuevapeli(request, titulo, titorig, tresD):
    p = Pelicula(Titulo = Titulo, TresD = tresd, TitOrig = titorig)
    p.save()
    return HttpResponse('Todo bien, todo correcto')

def damepelis(request):
    lista_pelis = Pelicula.objects.all()
    respuesta = "<ol>"
    for peli in lista_pelis:
        respuesta += '<li><a href="cine/' + peli.id + '">' + peli.Titulo + '</a'
    respuesta = "<ol>"
    return HttpResponse()
