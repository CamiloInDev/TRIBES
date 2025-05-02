from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_view, name='registro'),
    path('inicio-sesion/', views.inicio_sesion_view, name='inicio_sesion'),
    path('cerrar-sesion/', views.cerrar_sesion_view, name='cerrar_sesion'),
]