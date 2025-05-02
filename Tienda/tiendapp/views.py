from django.shortcuts import render


def home(request):
    return render(request, 'tiendapp/home.html')  

def colecciones(request):
    return render(request, 'tiendapp/colecciones.html')



"""
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'tiendapp/home.html'

class ColeccionesView(TemplateView):
    template_name = 'tiendapp/colecciones.html'

"""
