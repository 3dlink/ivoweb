from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    url(r'^configuraciongeneral/foto-perfil/$', login_required(Subir_foto_perfil), name='subir_foto_perfil'),
    url(r'^configuraciongeneral/foto-cover/$', login_required(Subir_foto_cover), name='subir_foto_cover'),
    url(r'^configuraciongeneral/$', login_required(Configuracion_General), name='configuracion_general'),
    url(r'^configuraciongeneral/cita/$', login_required(Configuracion_Cita), name='configuracion_cita'),
    url(r'^configuraciongeneral/experiencia/$', login_required(ConfiguracionExperiencia), name='configuracion_experiencia'),
    url(r'^configuraciongeneral/buscar-experiencia/$', login_required(Buscar_Experiencia), name='buscar_experiencia'),
    url(r'^configuraciongeneral/actualizar-seguridad/$', login_required(Configuracion_Seguriad_Actualizar), name='configuracion_Seguridad'),
    url(r'^configuraciongeneral/actualizar-general/$', login_required(Configuracion_General_Actualizar), name='configuracion_Seguridad'),
    url(r'^configuraciongeneral/idioma/borrar/$', login_required(Borrar_Idioma), name='borrar_Idioma'),
    url(r'^configuraciongeneral/idioma/$', login_required(Agregar_Idioma), name='agregar_Idioma'),
    url(r'^configuraciongeneral/educacion/$', login_required(Configuracion_Educacion), name='configuracion_educacion'),
    url(r'^configuraciongeneral/buscar-educacion/$', login_required(Buscar_Educacion), name='buscar_educacion'),
    url(r'^configuraciongeneral/actualizar-interes/$', login_required(Configuracion_Interes), name='configuracion_interes'),
    url(r'^mensajes/detalle/$', detalle_mensajes, name='detalle_mensajes'),
    url(r'^mensajes/enviar/$', enviar_mensajes, name='enviar_mensajes'),
    url(r'^mensajes/eliminar/$', eliminar_mensajes, name='eliminar_mensajes'),
    url(r'^([a-zA-Z0-9\-]+)/seguidores/$', seguidores, name='seguidores'),
    url(r'^([a-zA-Z0-9\-]+)/siguiendo/$', siguiendo, name='siguiendo'),    
    url(r'^([a-zA-Z0-9\-]+)/$', login_required(Perfil), name='perfil'),
    url(r'^subir_archivo/([a-z]+)/$', login_required(Subir_archivo_perfil), name='perfil'),
    url(r'^buscar-multimedia/([a-z]+)/$', login_required(Buscar_fotos), name='perfil_multimedia'),
    url(r'^borrar_archivos/$', login_required(borrar_archivos), name='borrar_archivos'),

]