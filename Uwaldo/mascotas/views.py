from rest_framework import viewsets
from .serializer import duenoSerializer, mascotaSerializer, citaSerializer, desparacitacionSerializer
from .models import dueno, mascota, cita, desparacitacion

# Create your views here.

class DuenoView(viewsets.ModelViewSet):
    serializer_class = duenoSerializer
    queryset = dueno.objects.all()
    
class MascotaView(viewsets.ModelViewSet):
    serializer_class = mascotaSerializer
    queryset = mascota.objects.all()
    
class CitaView(viewsets.ModelViewSet):
    serializer_class = citaSerializer
    queryset = cita.objects.all()
    
class DesparacitacionView(viewsets.ModelViewSet):
    serializer_class = desparacitacionSerializer
    queryset = desparacitacion.objects.all()