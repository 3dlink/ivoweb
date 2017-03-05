#serializer.py

from rest_framework import serializers
from frontend.models import TipoArte, User, UsuarioArte

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


