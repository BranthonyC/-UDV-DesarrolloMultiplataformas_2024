

from django.db import models

class Dueno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    estado = models.CharField(max_length=10)  

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    estado = models.CharField(max_length=10)  
    dueno = models.ForeignKey(Dueno, related_name='mascotas', on_delete=models.CASCADE)

class Cita(models.Model):
    fecha = models.DateTimeField()
    hora = models.TimeField()
    motivo = models.CharField(max_length=255)
    estado = models.CharField(max_length=10)  
    mascota = models.ForeignKey(Mascota, related_name='citas', on_delete=models.CASCADE)

class FichaDesparasitacion(models.Model):
    fecha = models.DateField()
    observaciones = models.TextField()
    estado = models.CharField(max_length=10)  
    mascota = models.ForeignKey(Mascota, related_name='fichas_desparasitacion', on_delete=models.CASCADE)

