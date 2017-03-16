from django import forms
from .models import Casting, Categoria

class FormRegistro(forms.ModelForm):
    
    class Meta:
        model = Casting
        exclude = ['imagen_principal', 'imagen_1', 'imagen_2', 'categoria','descripcion_breve', 'autor']
       
