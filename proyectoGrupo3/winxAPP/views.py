from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Temporada, Escuela, Personaje

# Create your views here.
def index(request):
    return HttpResponse('primera vista')

def listaTemporadas(request):
    temporadas = Temporada.objects.order_by('nombre')
    contexto = {'temporada_list': temporadas}
    return render(request, 'listaTemporadas.html', contexto)

def detalleTemporada(request, id_temporada):
    try:
        temporada = Temporada.objects.get(pk=id_temporada)
        escuelas = temporada.escuelas.all()

        cadenaDeTexto = f"Temporada: {temporada.nombre}\n"

        if escuelas.exists():
            cadenaDeTexto += "Escuelas:\n"
            for escuela in escuelas:
                cadenaDeTexto += f"- {escuela.nombre}\n"
        else:
            cadenaDeTexto += "No hay escuelas asociados a esta temporada."

        contexto = {'temporada_list': temporada}
        return render(request, 'detalleTemporada.html', contexto)
    except Temporada.DoesNotExist:
        return HttpResponseNotFound("Temporada no encontrada")


def listaEscuelas(request):
    escuelas = Escuela.objects.order_by('nombre')
    nombres_escuelas = ', '.join([escuela.nombre for escuela in escuelas])
    return HttpResponse(nombres_escuelas)

def detalleEscuela(request, id_escuela):
    try:
        escuela = Escuela.objects.get(pk=id_escuela)
        personajes = escuela.personajes.all()

        cadenaDeTexto = f"Escuela: {escuela.nombre}\n"

        if personajes.exists():
            cadenaDeTexto += "Personajes:\n"
            for personaje in personajes:
                cadenaDeTexto += f"- {personaje.nombre}\n"
        else:
            cadenaDeTexto += "No hay personajes asociados a esta escuela."

        return HttpResponse(cadenaDeTexto)
    except Escuela.DoesNotExist:
        return HttpResponseNotFound("Escuela no encontrada")
    

def listaPersonajes(request):
    personajes = Personaje.objects.order_by('nombre')
    nombres_personajes = ', '.join([personaje.nombre for personaje in personajes])
    return HttpResponse(nombres_personajes)

def detallePersonaje(request, id_personaje):
    try:
        personaje = Personaje.objects.get(pk=id_personaje)

        cadenaDeTexto = f"Personaje: {personaje.nombre}\n"

        return HttpResponse(cadenaDeTexto)
    except Personaje.DoesNotExist:
        return HttpResponseNotFound("Personaje no encontrado")