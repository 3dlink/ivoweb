from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,render_to_response
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import ugettext_lazy as _
from frontend.models import User, Etnia, Cabellos,Ojos, Seguidores
from .models import Multimedia, Experiencia, Educacion, Mensaje
from .forms import FormActualizarDatos, FormExperiencia, FormEducacion, FormMensaje
from core.UploadFile import UploadFile
from core.utils import getDatosActualizar
from frontend.funciones import form_invalid
from core.clases.ClassUsuario import Usuario
from django.db.models import Q
import json
from django.shortcuts import redirect


# Create your views here.


def Subir_foto_perfil(request):
    archivo = UploadFile(request.FILES['foto'], '', 'avatar')
    if not archivo.upload():
        return HttpResponse(json.dumps({'mensaje': str(archivo.mensaje), 'success': False}), content_type="application/json")

    User.objects.filter(uuid=request.user.uuid).update(
        avatar=archivo.getFile()
    )
    return HttpResponse(json.dumps({'mensaje': str(archivo.mensaje),'success': True}), content_type="application/json")


def Subir_foto_cover(request):
    archivo = UploadFile(request.FILES['foto'], '', 'portada')
    if not archivo.upload():
        return HttpResponse(json.dumps({'mensaje': str(archivo.mensaje),'success': False}), content_type="application/json")

    User.objects.filter(uuid=request.user.uuid).update(
        portada=archivo.getFile()
    )
    return HttpResponse(json.dumps({'mensaje': str(archivo.mensaje), 'success': True}), content_type="application/json")



def Configuracion_Seguriad_Actualizar(request):
    if request.method == 'POST':
        cambiar_pass = False
        if len(request.POST['email']) > 0:
            User.objects.filter(uuid=request.user.uuid, email=request.POST['correo']).update(
                email=request.POST['email']
            )
        if len(request.POST['email']) > 0:
            form_pass = PasswordChangeForm(request.user, request.POST)
            if form_pass.is_valid():
                form = form_pass.save(commit=False)
                form.save()
            else:
                messages.add_message(request, messages.WARNING, form_pass.errors)

        return HttpResponseRedirect('/perfil/configuraciongeneral/')

def Configuracion_Idioma_Actualizar(request):
    if request.method == 'POST':
        datos = getDatosActualizar(User, request)
        User.objects.filter(uuid=request.user.uuid).update(**datos)

        return HttpResponse(json.dumps({'mensaje': ''}), content_type="application/json")


def Configuracion_General_Actualizar(request):
    if request.method == 'POST':
        datos = getDatosActualizar(User, request)
        User.objects.filter(uuid=request.user.uuid).update(**datos)

        return HttpResponseRedirect('/perfil/configuraciongeneral/')


def Configuracion_General(request):
    cabellos = Cabellos.objects.all()
    ojos = Ojos.objects.all()
    etnias = Etnia.objects.all()
   

    data = User.objects.get(uuid=request.user.uuid)
    form_pass = PasswordChangeForm(request.user)
    form_pass.fields['old_password'].widget.attrs = {'required': 'required',
                                                'label': _('Contraseña actual')}
    form_pass.fields['new_password1'].widget.attrs = {'required': 'required',
                                                 'label': _('Nueva contraseña')}
    form_pass.fields['new_password2'].widget.attrs = {'required': 'required',
                                                 'label': _('Confirme su nueva contraseña')}
    print(data.id)
    print(Experiencia.objects.filter(usuario=data))
    context = {
        'form': FormActualizarDatos,
        'form_pass' : form_pass,
        'form_experiencia' : FormExperiencia,
        'form_educacion' : FormEducacion,
        'titulo': _('Actualizar datos'),
        'datos': data,
        'datos_educacion' :Educacion.objects.filter(usuario=data.id),
        'datos_experiencia': Experiencia.objects.filter(usuario=data.id),
        'etnias':etnias,
        'ojos':ojos,
        'cabellos':cabellos
    }
    
    return render(request, "perfiles/configuraciongeneral.html", context)

def ConfiguracionExperiencia(request):
    if request.method == 'POST':
        form = FormExperiencia(request.POST)
        if form.is_valid():
            experiencia = form.save(commit=False)
            experiencia.usuario = User.objects.get(uuid=request.POST['usuario'])
            experiencia.save()
            return HttpResponse(json.dumps({'success': True}), content_type="application/json")
        else:
            return HttpResponse(json.dumps(form_invalid(form)), content_type="application/json")

def Configuracion_Educacion(request):
    if request.method == 'POST':
        form = FormEducacion(request.POST)
        if form.is_valid():
            educacion = form.save(commit=False)
            educacion.usuario = User.objects.get(uuid=request.POST['usuario'])
            educacion.save()
            return HttpResponse(json.dumps({'success': True}), content_type="application/json")
        else:
            return HttpResponse(json.dumps(form_invalid(form)), content_type="application/json")


def Perfil(request, uuid):
    usuario = Usuario(uuid)
    
    datos_personales = usuario.getDatosPersonales()
    #a=User.objects.get(datos_personales)
    seguir = Seguidores.objects.filter(origen=request.user.id,destino=datos_personales.id)
    enviados = Mensaje.objects.filter(origen=request.user.id)
    recibidos = Mensaje.objects.filter(destino=request.user.id)
    
   
    if datos_personales.tipo_usuario == 'I':
        tema = 'azul'
    else:
        tema = 'naranja'

    context = {
        'datos_personales' : datos_personales,
        'educacion': usuario.getEducacion(),
        'experiencia' : usuario.getExperiencia(),
        'tema' : tema,
        'titulo': _('Perfil de usuario '),
        'usuario':usuario,
        'seguir':len(seguir),
        'enviados':enviados,
        'recibidos':recibidos
    }
    import pdb; pdb.set_trace()
    return render(request, "perfiles/perfil.html", context)

def Subir_archivo_perfil(request, tipo_archivo):
    nombre_archivo = request.FILES['archivo'].name
    cluster = tipo_archivo
    tipo = 'I'

    if tipo_archivo == 'image':
        cluster = 'imagenes'
        tipo = 'I'
    elif tipo_archivo == 'video':
        tipo = 'V'
    elif tipo_archivo == 'audio':
        tipo = 'A'

    archivo = UploadFile(request.FILES['archivo'], '', cluster)
    if not archivo.upload():
        return HttpResponse(json.dumps({'mensaje': str(archivo.mensaje)}), content_type="application/json")

    guardar_archivo = Multimedia(
        cluster=archivo.getCluster(),
        archivo=archivo.getNameFile(),
        nombre_archivo=nombre_archivo,
        tipo_archivo= tipo,
        usuario=User.objects.get(uuid=request.user.uuid)
    )
    guardar_archivo.save()
    return HttpResponse(json.dumps({'mensaje': ''}), content_type="application/json")

def Buscar_fotos(request, tipo_archivo):
    try:
        archivo = 'I'
        if tipo_archivo == 'image':
            archivo = 'I'
        elif tipo_archivo == 'video':
            archivo = 'V'
        elif tipo_archivo == 'audio':
            archivo = 'A'

        #import pdb; pdb.set_trace()
        #AQUI HAY PROBLEMA PORQUE BUSCA LOS ELEMENTOS DEL USUARIO LOGGEADO Y NO DEL USUARIO QUE SE ESTA VIENDO
        archivo_list = Multimedia.objects.filter(usuario=User.objects.get(uuid=request.user.uuid), tipo_archivo=archivo)
        paginator = Paginator(archivo_list, 9)
        page = request.GET.get('page')
        try:
            archivo_paginacion = paginator.page(page)
        except PageNotAnInteger:
            archivo_paginacion = paginator.page(1)
        except EmptyPage:
            archivo_paginacion = paginator.page(paginator.num_pages)

        #max_item_paginas = 6
        if tipo_archivo == 'image':
            respuesta = paginar_fotos(archivo_paginacion)

        if tipo_archivo == 'audio':
            respuesta = paginar_audio(archivo_paginacion)

        return HttpResponse(json.dumps({'mensaje': '', 'archivos':respuesta['contenido_paginacion'],
                                        'item_paginas' : respuesta['pie_paginacion']}), content_type="application/json")

    except ObjectDoesNotExist:

        return HttpResponse(json.dumps({'mensaje': 'no datos'}), content_type="application/json")

def paginar_audio(audio_paginacion):
    xHTML_Paginas = ''
    for nro in range(1, int(audio_paginacion.paginator.num_pages) + 1):
        if nro == audio_paginacion.number:
            xHTML_Paginas += '<li style = "cursor:pointer;" onclick = "paginacion_fotos(' + str(
                nro) + ', 1)"><span class="icon_circle-slelected"></span></li>'
        else:
            xHTML_Paginas += '<li style = "cursor:pointer;" onclick = "paginacion_fotos(' + str(
                nro) + ', 1)"><span class="icon_circle-empty"></span></li>'

    xHTML = ''
    indx = 1
    for audio in audio_paginacion:
        xHTML += '<div class="col-md-12">'
        xHTML += '	<div class="ivo-mensaje-contenedorAudio ivo-mensaje-contenedorAudio-noBorde ivo-contenedorAudio-bck1">'
        xHTML += '		<div class="ivo-mensaje-contenedorAudio-carga" id = "progreso_audio-'+str(indx)+'" style="width: 0%;"></div>'
        xHTML += '		<div class="ivo-mensaje-contenedorAudio-contenido">'
        xHTML += '			<div>'
        xHTML += '				<span class="arrow_triangle-right_alt ivo-font-naranja play_audio" id = "'+str(indx)+'" audio = "/media/' + audio.cluster + audio.archivo + '"></span>'
        xHTML += '			</div>'
        xHTML += '			<h5>'+audio.nombre_archivo+'</h5>'
        xHTML += '		</div>'
        xHTML += '		<div class="ivo-mensaje-contenedorAudio-contenido2">'
        xHTML += '			<span class="tiempo" id = "tiempo_audio-'+str(indx)+'">00:00</span>'
        xHTML += '		</div>'
        xHTML += '	</div>'
        xHTML += '</div>'
        indx = indx + 1

    return {'pie_paginacion' : xHTML_Paginas, 'contenido_paginacion': xHTML}

def paginar_fotos(fotos_paginacion):
    xHTML_Paginas = ''
    for nro in range(1, int(fotos_paginacion.paginator.num_pages) + 1):
        if nro == fotos_paginacion.number:
            xHTML_Paginas += '<li style = "cursor:pointer;" onclick = "paginacion_fotos(' + str(
                nro) + ', 1)"><span class="icon_circle-slelected"></span></li>'
        else:
            xHTML_Paginas += '<li style = "cursor:pointer;" onclick = "paginacion_fotos(' + str(
                nro) + ', 1)"><span class="icon_circle-empty"></span></li>'

    xHTML = ''
    for foto in fotos_paginacion:
        xHTML += '<div class="col-lg-4 col-md-4 col-xs-6 thumb">'
        xHTML += '   <a style = "background-image:url(/media/' + foto.cluster + 'sm_' + foto.archivo + '); background-position:50% 25%; background-size:cover;" class="thumbnail ivo-perfil-galeria-item " href="/media/' + foto.cluster + '' + foto.archivo + '" data-gallery>'

        xHTML += '<div class="ivo-perfil-galeria-hover ivo-back-trs-azulClaro"><div><span class="arrow_expand"></span></div></div>'
        xHTML += '   </a>'
        xHTML += '</div>'

    return {'pie_paginacion': xHTML_Paginas, 'contenido_paginacion': xHTML}

def Mensajes(request):
    import pdb; pdb.set_trace()      
    return render(request,"perfiles/enviar_mensaje.html",{})


# OJO   OJO    OJO     OJO     OJO   OJO 
# NECESITO QUE SEA AJAX PARA PODER MANTENERME EN LA MISMA PAG¿INA
def enviar_mensajes(request):
    if request.method == 'POST':   
       
        mensaje=''
        form = FormMensaje(request.POST, request.FILES)        
        if form.is_valid():
            registro = form.save(commit =False)
            registro.destino = User.objects.get(email=request.POST['destino'])
            registro.origen = request.user
            registro.save()             
            mensaje = {'mensaje': str(_('Mensaje Enviado')), 'success': True}       
        else:
            mensaje = {'mensaje': str(_('No se ha podido enviar el mensaje')), 'success': False}
    return redirect("artistadashboard")



# OJO   OJO    OJO     OJO     OJO   OJO 
# NECESITO QUE SEA AJAX PARA PODER MANTENERME EN LA MISMA PAG¿INA
def eliminar_mensajes(request):
    if request.method == 'POST':         
        mensaje=''
        
        Mensaje.objects.filter(id=request.POST['idmensaje']).delete()
        mensaje = {'mensaje': str(_('Mensaje eliminado')), 'success': True}  

    #        mensaje = {'mensaje': str(_('No se ha podido enviar el mensaje')), 'success': False}
    #return redirect("artistadashboard")
    return HttpResponse(json.dumps(mensaje), content_type="application/json")


def seguidores(request,uuid):

    lista = Seguidores.objects.filter(destino=User.objects.get(uuid=uuid))
    paginator = Paginator(lista, 15)
    page = request.GET.get('page',1)
    try:
        seguidores = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        seguidores = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        seguidores = paginator.page(paginator.num_pages)
        #import pdb;   pdb.set_trace()
    return render_to_response("seguidores/seguidores.html", {"seguidores": seguidores })


def siguiendo(request,uuid):

    lista = Seguidores.objects.filter(destino=User.objects.get(uuid=uuid))
    paginator = Paginator(lista, 15)
    page = request.GET.get('page',1)
    try:
        seguidores = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        seguidores = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        seguidores = paginator.page(paginator.num_pages)
        #import pdb;   pdb.set_trace()
    return render_to_response("seguidores/siguiendo.html", {"seguidores": seguidores })




