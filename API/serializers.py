#serializer.py

from rest_framework import serializers
from frontend.models import TipoArte, User, UsuarioArte, UsuarioArteGenero, GeneroArtistico
from rest_framework.validators import UniqueValidator

#QUERYLOCO
# User.objects.get(email=UsuarioArte.objects.get(id=1).id_usuario).first_name

class TalentosSerializer(serializers.ModelSerializer):
	class Meta:
		model = TipoArte
		fields = ("__all__")


class LoginSerializer (serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ("__all__")


class UsuarioArteSerializer (serializers.ModelSerializer):
	class Meta:
		model = UsuarioArte
		fields = ("id_usuario",)


class RelacionSerializer(serializers.ModelSerializer):
	class Meta:
		model = UsuarioArteGenero
		fields = ('id_usuario', 'id_genero')


# 	EL URL ESTA MAL.. REVISAR
class GeneroSerializer(serializers.ModelSerializer):
	user_name=serializers.ReadOnlyField(source='id_usuario.get_full_name', read_only=True)
	genero= serializers.ReadOnlyField(source='id_genero.name', read_only=True)
	arte= serializers.ReadOnlyField(source='id_genero.id_tipo_arte.name', read_only=True)
	url=  serializers.ReadOnlyField(source='id_usuario.get_absolute_url', read_only=True)
	avatar= serializers.ReadOnlyField(source='id_usuario.avatar.url', read_only=True)
	class Meta:
		model= UsuarioArteGenero
		fields=('genero', 'user_name', 'arte', 'url', 'avatar')
		




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
		user.save()
		return user

	class Meta:
		model = User
		fields = ('tipo_usuario', 'usuario', 'email', 'password')
		write_only_fields = ('password',)



