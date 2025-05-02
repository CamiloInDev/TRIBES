from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Nombre de usuario'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Correo electrónico'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Contraseña'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Confirmar contraseña'
        })