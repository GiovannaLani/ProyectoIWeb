from django.db import models

# Create your models here.
class Temporada(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Escuela(models.Model):
    nombre = models.CharField(max_length=100)
    temporada = models.ForeignKey(Temporada, related_name='escuelas', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    escuela = models.ForeignKey(Escuela, related_name='personajes', on_delete=models.CASCADE)
    image_url = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.nombre