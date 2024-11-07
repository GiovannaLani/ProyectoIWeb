from django.db import models

# Create your models here.
class Temporada(models.Model):
    nombre = models.CharField(max_length=100)
    numeroTemporada = models.IntegerField(blank=True, null=True)
    numeroEpisodios = models.IntegerField(blank=True, null=True)
    fechaEstreno = models.DateField(blank=True, null=True)
    fechaFinal = models.DateField(blank=True, null=True)
    sinopsis = models.CharField(max_length= 10000,blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Escuela(models.Model):
    nombre = models.CharField(max_length=100)
    primeraAparicion = models.CharField(max_length=300,blank=True, null=True)
    especialidad = models.CharField(max_length=100,blank=True, null=True)
    localizacion = models.CharField(max_length=100,blank=True, null=True)
    directora = models.CharField(max_length=100,blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    temporadas = models.ManyToManyField(Temporada, related_name='escuelas')

    def __str__(self):
        return self.nombre
    
class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    clase = models.CharField(max_length=100,blank=True, null=True)
    genero = models.CharField(max_length=100,blank=True, null=True)
    cumpleaños = models.DateField(blank=True, null=True)
    afiliacion = models.CharField(max_length=100,blank=True, null=True)
    poderes = models.CharField(max_length=500,blank=True, null=True)
    origen = models.CharField(max_length=100,blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    escuela = models.ForeignKey(Escuela, related_name='personajes', on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre