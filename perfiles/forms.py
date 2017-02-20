from django import forms
from django.contrib.auth.forms import UserChangeForm

from frontend.models import User
from perfiles.models import Experiencia, Educacion


class FormActualizarDatos(forms.ModelForm):   
    class Meta:
        model = User
        exclude = ['empresa_provedor', 'razon_social', 'direccion', 'website', 'sector', 'username','email','tipo_usuario',
                   'is_staff','is_active','last_login','is_superuser','groups','permiss', 'user_permissions', 'password',
                   'date_joined','idioma']

class FormExperiencia(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['trabajo_actual'].widget.attrs.update({'class': 'regular-radio','id' : 'radio-1-2'})

    class Meta:
        model = Experiencia
        exclude = ['usuario']

class FormEducacion(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['estudiando_actualmente'].widget.attrs.update({'class': 'regular-radio','id' : 'radio-1-1'})

    class Meta:
        model = Educacion
        exclude = ['usuario']