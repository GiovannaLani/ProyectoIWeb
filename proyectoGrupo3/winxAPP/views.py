from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Temporada, Escuela, Personaje
from django.views.generic import ListView,DetailView

# Create your views here.
def index(request):
    return render(request, 'index.html')

class listaTemporadas(ListView):
    model = Temporada
    template_name = "listaTemporadas.html"
    context_object_name="temporada_list"
    queryset=Temporada.objects.order_by("numeroTemporada")

class detalleTemporada(DetailView):
	model= Temporada
	template_name = "detalleTemporada.html"

class listaEscuelas(ListView):
    model = Escuela
    template_name = "listaEscuelas.html"
    context_object_name="escuela_list"
    queryset=Escuela.objects.order_by("nombre")
    
class detalleEscuela(DetailView):
	model= Escuela
	template_name = "detalleEscuela.html"

class listaPersonajes(ListView):
    model = Personaje
    template_name = "listaPersonajes.html"
    context_object_name="personaje_list"
    queryset=Personaje.objects.order_by("nombre")
    
class detallePersonaje(DetailView):
	model= Personaje
	template_name = "detallePersonaje.html"
