from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='Home'),
    path('colecciones/', views.colecciones, name='colecciones'),
]


