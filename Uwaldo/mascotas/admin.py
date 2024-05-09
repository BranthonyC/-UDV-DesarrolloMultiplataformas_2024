from django.contrib import admin
from .models import dueno, mascota, cita, desparacitacion

# Register your models here.
admin.site.register(dueno)
admin.site.register(mascota)
admin.site.register(cita)
admin.site.register(desparacitacion)

