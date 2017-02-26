#serializer.py

from rest_framework import serializers
from .models import TipoArte, User


class GeneroSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = TipoArte
		fields = ("__all__")

class API_sesion (serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('first_name', 'tipo_usuario')