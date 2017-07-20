from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from frontend.models import *
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
     
#LISTADO DE ARTISTAS GENERAL, POR CATEGORIA Y SUS GENEROS ARTISTICOS

class TalentosView(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser,)

    def get(self,request):
        all_users = UsuarioArteGenero.objects.all()
        serializer = GeneroSerializer(all_users, many = True)
        return Response(serializer.data)

class TalentosTipoView(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser,)

    def get(self,request,idcategoria):
        categoria = TipoArte.objects.get(name=idcategoria)
        generos = GeneroArtistico.objects.filter(id_tipo_arte=categoria).values('id')
        all_users = UsuarioArteGenero.objects.filter(id_genero__in=generos)
        serializer = GeneroSerializer(all_users, many = True)
        return Response(serializer.data)

class TipoArteView(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser,)  

    def get(self,request):
        tipo_arte = TipoArte.objects.all()
        serializer= TipoArteSerializer(tipo_arte, many=True)
        
        return Response(serializer.data )


# LISTADO DE PROVEEDORES GENERAL, POR CATEGORIA, Y SUS SECTORES
class ProveedoresView(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser,)

    def get(self,request):
        industria = Industria.objects.filter(tipo='P').values_list('id',flat=True)
        all_users = SectorIndustria.objects.filter(id_sector__in=industria)
        serializer= MenuIndustriaSerializer(all_users, many=True)
        return Response(serializer.data)

class ProveedoresTipoView(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser,)

    def get(self,request,idcategoria):
        industria = Industria.objects.filter(nombre=idcategoria)
        all_users = SectorIndustria.objects.filter(id_sector=industria)
        serializer = MenuIndustriaSerializer(all_users, many = True)
        return Response(serializer.data)



class TipoIndustriaView(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser,)  

    def get(self,request):
        tipo_industria = Industria.objects.filter(tipo='P')
        serializer= TipoIndustriaSerializer(tipo_industria, many=True)
        
        return Response(serializer.data )


class CastingsView(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser,)

    def get(self,request):
        all_casting = Casting.objects.filter(fecha_fin__gte=date.today())       
        serializer= CastingSerializer(all_casting, many=True)
        return Response(serializer.data)

class CastingsTipoView(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser,)

    def get(self,request,idcategoria):
        categoria = Filtro.objects.filter(id_talento=idcategoria).values_list('id_casting',flat=True)
        all_casting = Casting.objects.filter(id__in=categoria,fecha_fin__gte=date.today())
        serializer= CastingSerializer(all_casting, many=True)
        return Response(serializer.data)



class TipoArteView(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser,)  

    def get(self,request):
        tipo_arte = TipoArte.objects.all()
        serializer= TipoArteSerializer(tipo_arte, many=True)
        
        return Response(serializer.data )



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
        Us = User.objects.get(email=email)       
        if Us.tipo_usuario == 'A':
            Usuario = UsuarioArteGenero.objects.get(id_usuario=Us.id)
            serializer= MenuArtistaSerializer(Usuario, many=False)        
        else:
            Usuario = SectorIndustria.objects.get(id_usuario=Us.id)
            serializer= MenuIndustriaSerializer(Usuario, many=False)
        return Response(serializer.data) 
        
class NumeroSeguidoresView(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser,)
    def get(self,request,email):
            user = User.objects.get(email=email)
            numero_seguidores = len(Seguidores.objects.filter(destino=user))
            return Response({'numero_seguidores': numero_seguidores}) 

#FALTA DEVOLVER EL NUMERO DE MENSAJES