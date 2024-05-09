from django.db import models

# Create your models here.

class Dueno(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    correo_electronico = models.EmailField()

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido} - {self.correo_electronico}'

class Mascota(models.Model):
    
    id = models.AutoField(primary_key=True)
    dueno = models.ForeignKey(Dueno, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    tipo_animal = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.nombre} - {self.raza}'

class FichaDesparasitacion(models.Model):
    id = models.AutoField(primary_key=True)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha = models.DateField()
    desparasitante = models.CharField(max_length=100)
    dosis = models.CharField(max_length=100)
    notas = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.mascota} - {self.fecha}'

class Cita(models.Model):
    id = models.AutoField(primary_key=True)
    dueno = models.ForeignKey(Dueno, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha = models.DateField()
    motivo = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f'{self.dueno} - {self.mascota} - {self.fecha}'
