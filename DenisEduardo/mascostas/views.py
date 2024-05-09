from django.shortcuts import render
from rest_framework import viewsets
from .serializer import DuenoSerializer,MascotaSerializer,FichaDesparasitacionSerializer,CitaSerializer
from .models import Dueno,Mascota,FichaDesparasitacion,Cita

# Create your views here.
class DuenoView(viewsets.ModelViewSet):
    serializer_class = DuenoSerializer
    queryset = Dueno.objects.all()

class MascotaView(viewsets.ModelViewSet):
    serializer_class = MascotaSerializer
    queryset = Mascota.objects.all()

class FichaDesparacitacionView(viewsets.ModelViewSet):
    serializer_class = FichaDesparasitacionSerializer
    queryset = FichaDesparasitacion.objects.all()

class CitaView(viewsets.ModelViewSet):
    serializer_class = CitaSerializer
    queryset = Cita.objects.all()