from django import forms
from .models import Casting, Categoria

class FormRegistro(forms.ModelForm):
    
    class Meta:
        model = Casting
        exclude = ['imagen_principal','descripcion_breve', 'autor']
       
