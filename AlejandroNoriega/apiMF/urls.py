from django.urls import path
from .views import DuenoList, DuenoDetail, MascotaList, MascotaDetail, CitaList, CitaDetail, DesparasitacionList, DesparasitacionDetail

urlpatterns = [
    path('api/duenos/', DuenoList.as_view()),
    path('api/duenos/<int:pk>/', DuenoDetail.as_view()),
    path('api/mascotas/', MascotaList.as_view()),
    path('api/mascotas/<int:pk>/', MascotaDetail.as_view()),
    path('api/citas/', CitaList.as_view()),
    path('api/citas/<int:pk>/', CitaDetail.as_view()),
    path('api/desparasitaciones/', DesparasitacionList.as_view()),
    path('api/desparasitaciones/<int:pk>/', DesparasitacionDetail.as_view()),
]