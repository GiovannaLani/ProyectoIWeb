from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('temporadas/', views.listaTemporadas.as_view(), name='listaTemporadas'),
    path('temporadas/<int:pk>/', views.detalleTemporada.as_view(), name='detalleTemporada'),
    path('escuelas/', views.listaEscuelas.as_view(), name='listaEscuelas'),
    path('escuelas/<int:pk>/', views.detalleEscuela.as_view(), name='detalleEscuela'),
    path('personajes/', views.listaPersonajes.as_view(), name='listaPersonajes'),
    path('personajes/<int:pk>/', views.detallePersonaje.as_view(), name='detallePersonaje'),
]