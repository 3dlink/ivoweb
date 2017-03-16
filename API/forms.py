from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from frontend.models import User



class FormRegistro(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'usuario', 'tipo_usuario', 'password']
        