from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class RegistroUsuarioForm(UserCreationForm):
    email     = forms.EmailField(required=True)
    telefono  = forms.CharField(max_length=20, required=False)
    direccion = forms.CharField(max_length=255, required=False)

    class Meta:
        model  = CustomUser
        fields = ("username", "email", "telefono", "direccion", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email     = self.cleaned_data["email"]
        user.telefono  = self.cleaned_data["telefono"]
        user.direccion = self.cleaned_data["direccion"]
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "username":    "Nombre de usuario",
            "email":       "Correo electrónico",
            "telefono":    "Teléfono",
            "direccion":   "Dirección",
            "password1":   "Contraseña",
            "password2":   "Confirmar contraseña",
        }
        for field_name, placeholder in placeholders.items():
            if field_name in self.fields:
                self.fields[field_name].widget.attrs.update({
                    "class": "input-field",
                    "placeholder": placeholder,
                })
