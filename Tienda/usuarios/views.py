from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import RegistroUsuarioForm


def registro_view(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("Home")
    else:
        form = RegistroUsuarioForm()
    return render(request, "usuarios/registro.html", {"form": form})

def inicio_sesion_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect("Home")
    else:
        form = AuthenticationForm()
    
    form.fields['username'].widget.attrs.update({
        'class': 'input-field',
        'placeholder': 'Nombre de usuario'
    })
    form.fields['password'].widget.attrs.update({
        'class': 'input-field',
        'placeholder': 'Contraseña'
    })
    return render(request, "usuarios/inicio_sesion.html", {"form": form})

def cerrar_sesion_view(request):
    logout(request)
    return redirect("Home")

# Create your views here.
