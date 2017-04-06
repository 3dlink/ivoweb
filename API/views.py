from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistroSerializer, TalentosSerializer, LoginSerializer, MultimediaSerializer, GeneroSerializer, UsuarioExpSerializer, UsuarioImgSerializer, MenuArtistaSerializer, MenuIndustriaSerializer
from frontend.models import User, TipoArte, GeneroArtistico,generateUUID, UsuarioArteGenero, UsuarioArte
from django.contrib.auth import authenticate, login, logout
from django.http import  JsonResponse
from .forms import FormRegistro
import json
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
from perfiles.models import Experiencia, Educacion, Multimedia
# Create your views here.



class RegistroView(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser,)  

    def post(self, request, format='json'):
        #import pdb;   pdb.set_trace()
        payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        encode_handler = api_settings.JWT_ENCODE_HANDLER
        serializer = RegistroSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            userfinal = authenticate(email=request.data['email'], password=request.data['password'])
            
            if user:
                payload = payload_handler(userfinal)
                token = encode_handler(payload)
                json = serializer.data
                json['token'] = token
                
                return Response(json, status=status.HTTP_201_CREATED)  
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     


class TalentosView(APIView):

    def get(self,request):
        all_users = UsuarioArteGenero.objects.all()
        serializer = TalentosSerializer(all_users, many = True)
        return Response(serializer.data)



class Usuario_ArteView(APIView):
# User.objects.get(email=UsuarioArte.objects.get(id=1).id_usuario).first_name
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser,)  

    def get(self,request):
        arte= TipoArte.objects.get(name=request.GET['arte']).id
        UsuarioArt = UsuarioArte.objects.filter(id=arte)
        Usuario = User.objects.filter(id=UsuarioArt)
        serializer = LoginSerializer(Usuario, many = True)
        return Response(serializer.data)


class ExampleView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request):
        data = {
            'id': request.user.id,
            'email': request.user.email,
            'token': str(request.auth)
        }
        return Response(data)


class GenerosView(APIView):
# User.objects.get(email=UsuarioArte.objects.get(id=1).id_usuario).first_name
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, )
    parser_classes = (JSONParser,)  

    def get(self,request):
        user_genero= UsuarioArteGenero.objects.all()
        serializer= GeneroSerializer(user_genero, many=True)
        
        return Response(serializer.data )


class UserCategoriaView(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser,)  


    def get(self,request,idcategoria):
        arte= TipoArte.objects.get(name=idcategoria)       
        user_arte= GeneroArtistico.objects.filter(id_tipo_arte=arte.id)
        Usuario = UsuarioArteGenero.objects.filter(id_genero=user_arte)
        serializer= GeneroSerializer(Usuario, many=True)
    
        #import pdb;   pdb.set_trace()
        return Response(serializer.data )


class UsuarioView(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser,)  


    def get(self,request,email,tab):
        Usuario = User.objects.get(email=email)   
        if tab=='experiencia':                     
            serializer= UsuarioExpSerializer(Usuario, many=False)        
            #import pdb;   pdb.set_trace()         

        elif tab=='imagen':            
            Lista=Multimedia.objects.filter(usuario=Usuario, tipo_archivo='I')
            serializer= MultimediaSerializer(Lista, many=True)
        elif tab=='video':            
            Lista=Multimedia.objects.filter(usuario=Usuario, tipo_archivo='V')
            serializer= MultimediaSerializer(Lista, many=True)
        elif tab=='audio':            
            Lista=Multimedia.objects.filter(usuario=Usuario, tipo_archivo='A')
            serializer= MultimediaSerializer(Lista, many=True)
        return Response(serializer.data)

class MenuUsuarioView(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser,)  

    def get(self,request,email):
        Usuario = User.objects.get(email=email)
        if Usuario.tipo_usuario == 'A':
            serializer= MenuArtistaSerializer(Usuario, many=False)        
        else:
            serializer= MenuIndustriaSerializer(Usuario, many=False)
        return Response(serializer.data) 
        

# """
# /*Estilo del reloj Atras*/
#     var $clock = $('#clock-atras');
    
#     $clock.countdown('2017-04-15 23:59:59', function(event) {
#     $(this).html(event.strftime('<p><span class="block-orange"><img src='+base_url+'/assetsfrontend/img/ico-calendario.png alt=""/> Quedan %D días </span> %H:%M:%S </p>'));
#     });
# """