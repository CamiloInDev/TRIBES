from django.urls import path
from . import views

# app_name = 'tiendapp'  # Opcional: Esto crea un namespace para tus URLs

urlpatterns = [
    path('', views.home, name='Home'),
    path('colecciones/', views.colecciones, name='colecciones'),
]