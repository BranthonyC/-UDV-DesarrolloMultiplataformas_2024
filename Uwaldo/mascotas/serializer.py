from rest_framework import serializers
from .models import dueno, mascota, cita, desparacitacion

class duenoSerializer(serializers.ModelSerializer):
    class Meta:
        model = dueno
        fields = '__all__'
        
class mascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = mascota
        fields = '__all__'
        
class citaSerializer(serializers.ModelSerializer):
    class Meta:
        model = cita
        fields = '__all__'
        
class desparacitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = desparacitacion 
        fields = '__all__'