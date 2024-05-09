from django.urls import path, include
from rest_framework import routers
from mascotas import views

#APIS
router = routers.DefaultRouter()
router.register(r'dueno', views.DuenoView, 'dueno')
router.register(r'mascotas', views.MascotaView, 'mascota')
router.register(r'cita', views.CitaView, 'cita')
router.register(r'desparacitacion', views.DesparacitacionView, 'desparacitacion')

urlpatterns = [
    path("api/", include(router.urls))
]

