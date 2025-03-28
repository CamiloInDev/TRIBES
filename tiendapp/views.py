from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'tiendapp/home.html')  

def colecciones(request):
    return render(request, 'tiendapp/colecciones.html')