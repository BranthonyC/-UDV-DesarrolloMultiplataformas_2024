from django.db import models

# Create your models here.

class dueno (models.Model):
    id_dueno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f'{self.nombre} - {self.direccion} - {self.telefono}'
    
class mascota (models.Model):
    id_mascota = models.AutoField(primary_key=True)
    dueno = models.ForeignKey(dueno, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    especie = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    edad = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.nombre} - {self.especie} - {self.raza}'
    
class cita (models.Model):
    id_cita = models.AutoField(primary_key=True)
    dueno = models.ForeignKey(dueno, on_delete=models.CASCADE)
    mascota = models.ForeignKey(mascota, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    razon = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f'{self.dueno} - {self.fecha} - {self.hora} - {self.razon}'
    
class desparacitacion (models.Model):
    id_desparacitacion = models.AutoField(primary_key=True)
    mascota = models.ForeignKey(mascota, on_delete=models.CASCADE)
    fecha = models.DateField() 
    tipo = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f'{self.mascota} - {self.fecha} - {self.id_desparacitacion}'
    