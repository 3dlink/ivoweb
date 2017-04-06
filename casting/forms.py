from django import forms
from .models import Casting, Categoria, Audicion

class FormRegistro(forms.ModelForm):
    
    class Meta:
        model = Casting
        exclude = ['imagen_principal','descripcion_breve', 'autor']


class FormAudicion(forms.ModelForm):
	
	class Meta:
		model = Audicion
		exclude = ['id_usuario', 'id_casting']
    		
       
