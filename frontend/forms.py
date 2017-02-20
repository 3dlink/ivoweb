from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from frontend.models import User

class FormRegistro(UserCreationForm):
    #INPUT_FORMAT = (
    #    ('%d/%m/%Y', '%m/%d/%Y')
    #)
    #fecha_nacimiento = forms.DateField(input_formats=INPUT_FORMAT)
    class Meta:
        model = User
        exclude = ['empresa_provedor', 'razon_social', 'direccion', 'website',
                    'telefono', 'pasaporte', 'visa','uuid','biografia','avatar',
                   'is_staff','is_active','last_login','is_superuser','groups','permiss', 'user_permissions',
                   'password','date_joined','idioma']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',
        }


class FormRegistroIndustria(UserCreationForm):
    class Meta:
        model = User
        fields = ['empresa_provedor', 'razon_social', 'direccion', 'website', 'facebook', 'twitter', 
        'instagram', 'usuario', 'genero', 'tipo_usuario', 'email']


class FormRegistroFan(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'facebook', 'twitter', 
        'instagram', 'fecha_nacimiento','genero','usuario', 'tipo_usuario', 'email']
        
        labels= {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',
        }
    