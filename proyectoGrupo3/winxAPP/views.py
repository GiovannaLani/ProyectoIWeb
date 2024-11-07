from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Temporada, Escuela, Personaje

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listaTemporadas(request):
    temporadas = Temporada.objects.order_by('nombre')
    contexto = {'temporada_list': temporadas}
    return render(request, 'listaTemporadas.html', contexto)

def detalleTemporada(request, id_temporada):
    try:
        temporada = Temporada.objects.get(pk=id_temporada)
        contexto = {'temporada': temporada}
        return render(request, 'detalleTemporada.html', contexto)
    except Temporada.DoesNotExist:
        return HttpResponseNotFound("Temporada no encontrada")


def listaEscuelas(request):
    escuelas = Escuela.objects.order_by('nombre')
    contexto = {'escuela_list': escuelas}
    return render(request, 'listaEscuelas.html', contexto)

def detalleEscuela(request, id_escuela):
    try:
        escuela = Escuela.objects.get(pk=id_escuela)
        contexto = {'escuela': escuela}
        return render(request, 'detalleEscuela.html', contexto)
    except Escuela.DoesNotExist:
        return HttpResponseNotFound("Escuela no encontrada")
    

def listaPersonajes(request):
    personajes = Personaje.objects.order_by('nombre')
    contexto = {'personaje_list': personajes}
    return render(request, 'listaPersonajes.html', contexto)

def detallePersonaje(request, id_personaje):
    try:
        personaje = Personaje.objects.get(pk=id_personaje)
        contexto = {'personaje': personaje}
        return render(request, 'detallePersonaje.html', contexto)
    except Personaje.DoesNotExist:
        return HttpResponseNotFound("Personaje no encontrado")