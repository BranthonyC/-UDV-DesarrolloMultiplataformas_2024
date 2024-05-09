from django.shortcuts import render

from rest_framework import generics
from .models import Dueno, Mascota, Cita, FichaDesparasitacion
from .serializers import DuenoSerializer, MascotaSerializer, CitaSerializer, DesparasitacionSerializer

# Dueños
class DuenoList(generics.ListCreateAPIView):
    queryset = Dueno.objects.all()
    serializer_class = DuenoSerializer

class DuenoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dueno.objects.all()
    serializer_class = DuenoSerializer

# Mascotas
class MascotaList(generics.ListCreateAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class MascotaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

# Citas
class CitaList(generics.ListCreateAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

class CitaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

# Desparasitaciones
class DesparasitacionList(generics.ListCreateAPIView):
    queryset = FichaDesparasitacion.objects.all()
    serializer_class = DesparasitacionSerializer

class DesparasitacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FichaDesparasitacion.objects.all()
    serializer_class = DesparasitacionSerializer
