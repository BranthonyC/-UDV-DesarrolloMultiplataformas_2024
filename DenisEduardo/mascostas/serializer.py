from rest_framework import serializers
from .models import Dueno,Mascota,FichaDesparasitacion,Cita

class DuenoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dueno
        fields = '__all__'

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'

class FichaDesparasitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichaDesparasitacion
        fields = '__all__'

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'