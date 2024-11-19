from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('temporadas/', views.listaTemporadas, name='listaTemporadas'),
    path('temporadas/<int:id_temporada>/', views.detalleTemporada, name='detalleTemporada'),
    path('escuelas/', views.listaEscuelas, name='listaEscuelas'),
    path('escuelas/<int:id_escuela>/', views.detalleEscuela, name='detalleEscuela'),
    path('personajes/', views.listaPersonajes, name='listaPersonajes'),
    path('personajes/<int:id_personaje>/', views.detallePersonaje, name='detallePersonaje'),
]