from mascostas import views
from django.urls import include, path
from rest_framework import routers

# vista de las api.
router = routers.DefaultRouter()

router.register(r'dueno', views.DuenoView, 'dueno')
router.register(r'mascotas', views.MascotaView, 'mascota')
router.register(r'fichadesparacitacion', views.FichaDesparacitacionView, 'fichadesparacitacion')
router.register(r'citas', views.CitaView, 'cita')

urlpatterns = [
    path ('api/', include(router.urls))
]