from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from frontend.models import User, Seguidores
from django.contrib.auth import authenticate

class FormRegistro(UserCreationForm):
    
    class Meta:
        model = User
        exclude = ['empresa_provedor', 'razon_social', 'direccion', 'website',
                    'telefono', 'pasaporte', 'visa','uuid','biografia','avatar',
                   'is_staff','is_active','last_login','is_superuser','groups','permiss', 'user_permissions',
                   'password','date_joined','idioma', 'estatura', 'busto','cintura','cadera']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',
        }
        error_messages={

            'min_length': ("La contraseña es muy corta, debe ser de al menos 8 caracteres")
        }


class FormRegistroIndustria(UserCreationForm):
    class Meta:
        model = User
        fields = ['empresa_provedor', 'razon_social', 'direccion', 'website', 'facebook', 'twitter', 
        'instagram', 'usuario', 'genero', 'tipo_usuario', 'email', 'pais','telefono']

        error_messages={
            'password':{
                'min_length': ("La contraseña es muy corta, debe ser de al menos 8 caracteres"),
            },
            
        }


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


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("    Correo o contraseña no valido    ")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

class FormSeguir(forms.ModelForm):
    class Meta:
        model = Seguidores
        fields =("__all__")

class contactoForm(forms.Form):
    email = forms.EmailField(max_length=254, required=True)
    nombre = forms.CharField(required=True,max_length=30 )
    asunto = forms.CharField(required=True)
    mensaje = forms.CharField(required=True, widget=forms.Textarea)