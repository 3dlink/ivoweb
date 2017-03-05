from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TalentosSerializer, LoginSerializer, UsuarioArteSerializer
from frontend.models import User, TipoArte, GeneroArtistico,generateUUID, UsuarioArte
from django.contrib.auth import authenticate, login, logout
from django.http import  JsonResponse
import json
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class LoginView(APIView):

 
    def post(self, request):
        #import pdb;   pdb.set_trace()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            serializer = LoginSerializer(user)
            if user.is_active:
                #login(request, user)
                return JsonResponse(serializer.data,safe=False)
            else:
               # messages.add_message(request, messages.INFO, _('Cuenta de usuario inactiva'))
                return JsonResponse("{'status':'invactivo'}", safe=False)
        else:
            #messages.add_message(request, messages.INFO, _('Nombre de usuario o contraseña no valido'))
            return JsonResponse("{'status':'invalido'}",safe=False)



class TalentosView(APIView):

    def get(self,request):
        talentos = TipoArte.objects.all()
        serializer = TalentosSerializer(talentos, many = True)
        return Response(serializer.data)


# class UsuarioArteView(APIView):

# # User.objects.get(email=UsuarioArte.objects.get(id=1).id_usuario).first_name
# 	def get(self,request):
# 		arte= TipoArte.objects.get(name=request.GET['arte'])
# 		UsuarioArte = UsuarioArte.objects.get(id=arte.id)
# 		serializer = UsuarioArteSerializer(Usuario, many = False)
# 		return Response(serializer.data)

class Usuario_ArteView(APIView):
# User.objects.get(email=UsuarioArte.objects.get(id=1).id_usuario).first_name


	def get(self,request):
		arte= TipoArte.objects.get(name=request.GET['arte']).id
		UsuarioArt = UsuarioArte.objects.filter(id=arte)
		Usuario = User.objects.filter(id=UsuarioArt)
		serializer = LoginSerializer(Usuario, many = True)
		return Response(serializer.data)



