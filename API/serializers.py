#serializer.py

from rest_framework import serializers
from frontend.models import *
from perfiles.models import *
from casting.models import *
from rest_framework.validators import UniqueValidator
from datetime import date

#QUERYLOCO
# User.objects.get(email=UsuarioArte.objects.get(id=1).id_usuario).first_name


class LoginSerializer (serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ("__all__")



class TipoArteSerializer (serializers.ModelSerializer):

	class Meta:
		model = TipoArte
		fields = ("__all__")

class TipoIndustriaSerializer (serializers.ModelSerializer):

	class Meta:
		model = Industria
		fields = ("__all__")	


class GeneroSerializer(serializers.ModelSerializer):
	user_name=serializers.ReadOnlyField(source='id_usuario.get_full_name', read_only=True)
	genero= serializers.ReadOnlyField(source='id_genero.name', read_only=True)
	arte= serializers.ReadOnlyField(source='id_genero.id_tipo_arte.name', read_only=True)
	url=  serializers.ReadOnlyField(source='id_usuario.get_api_url', read_only=True)
	#avatar= serializers.ReadOnlyField(source='id_usuario.avatar.url', read_only=True)
	class Meta:
		model= UsuarioArteGenero
		fields=('genero', 'user_name', 'arte', 'url')


class CastingSerializer(serializers.ModelSerializer):
	#avatar= serializers.ReadOnlyField(source='id_usuario.avatar.url', read_only=True)
	class Meta:
		model= Casting
		fields=('titulo','descripcion','imagen_1')


class RegistroSerializer(serializers.ModelSerializer):
	tipo_usuario = serializers.CharField(max_length=1)
	email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
	usuario = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
	password = serializers.CharField(min_length=8, write_only=True)

	def create(self, validated_data):
		user = User.objects.create_user(validated_data['email'],
             validated_data['password'])
		user.usuario=validated_data['usuario']
		user.tipo_usuario=validated_data['tipo_usuario']
		user.uuid = generateUUID()
		user.save()
		return user

	class Meta:
		model = User
		fields = ('tipo_usuario', 'usuario', 'email', 'password')
		write_only_fields = ('password',)


class MultimediaSerializer(serializers.ModelSerializer):
	class Meta:
		model=Multimedia
		fields = ('absolute_url',)
		#fields=("__all__")



class ExperienciaSerializer(serializers.ModelSerializer):
	#usuario = UsuarioSerializer(many=False)
	class Meta:
		model = Experiencia
		fields = ("__all__")

class EducacionSerializer(serializers.ModelSerializer):
	#usuario = UsuarioSerializer(many=False)
	class Meta:
		model = Educacion
		fields = ("__all__")

class UsuarioExpSerializer(serializers.ModelSerializer):
	experiencia = ExperienciaSerializer(many=True)
	educacion = EducacionSerializer(many=True)
	class Meta:
		model = User
		fields=("__all__")

class UsuarioImgSerializer(serializers.ModelSerializer):
	multimedia = MultimediaSerializer(many=True)
	class Meta:
		model = User
		fields=("__all__")	


#DATOS BASICOS ARTISTA
class MenuArtistaSerializer(serializers.ModelSerializer):
	user_name=serializers.ReadOnlyField(source='id_usuario.get_full_name', read_only=True)
	genero= serializers.ReadOnlyField(source='id_genero.name', read_only=True)
	arte= serializers.ReadOnlyField(source='id_genero.id_tipo_arte.name', read_only=True)
	url=  serializers.ReadOnlyField(source='id_usuario.get_api_url', read_only=True)
	avatar= serializers.ReadOnlyField(source='id_usuario.avatar.url', read_only=True)
	class Meta:
		model= UsuarioArteGenero
		fields=('genero', 'user_name', 'arte', 'url', 'avatar')

class MenuIndustriaSerializer(serializers.ModelSerializer):	
	user_name=serializers.ReadOnlyField(source='id_usuario.empresa_provedor', read_only=True)
	sector= serializers.ReadOnlyField(source='id_sector.nombre', read_only=True)
	tipo= serializers.ReadOnlyField(source='id_genero.id_tipo_arte.name', read_only=True)
	url=  serializers.ReadOnlyField(source='id_usuario.get_api_url', read_only=True)
	#avatar= serializers.ReadOnlyField(source='id_usuario.avatar.url', read_only=True)
	class Meta:
		model= UsuarioArteGenero
		fields=('sector', 'user_name', 'url', 'tipo')
		

