from django.contrib import admin
from .models import Dueno,Mascota,FichaDesparasitacion,Cita

# Register your models here.
admin.site.register(Dueno)
admin.site.register(Mascota)
admin.site.register(FichaDesparasitacion)
admin.site.register(Cita)
