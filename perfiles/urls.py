from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    url(r'^configuraciongeneral/foto-perfil/$', login_required(Subir_foto_perfil), name='subir_foto_perfil'),
    url(r'^configuraciongeneral/$', login_required(Configuracion_General), name='configuracion_general'),
    url(r'^configuraciongeneral/experiencia/$', login_required(ConfiguracionExperiencia), name='configuracion_experiencia'),
    url(r'^configuraciongeneral/actualizar-seguridad/$', login_required(Configuracion_Seguriad_Actualizar), name='configuracion_Seguridad'),
    url(r'^configuraciongeneral/actualizar-general/$', login_required(Configuracion_General_Actualizar), name='configuracion_Seguridad'),
    url(r'^configuraciongeneral/idiomas/$', login_required(Configuracion_Idioma_Actualizar), name='configuracion_Idioma'),
    url(r'^configuraciongeneral/educacion/$', login_required(Configuracion_Educacion), name='configuracion_educacion'),

    
    url(r'^([a-zA-Z0-9\-]+)/$', login_required(Perfil), name='perfil'),
    url(r'^subir_archivo/([a-z]+)/$', login_required(Subir_archivo_perfil), name='perfil'),
    url(r'^buscar-multimedia/([a-z]+)/$', login_required(Buscar_fotos), name='perfil_multimedia'),
]