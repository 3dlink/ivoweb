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
from frontend.models import User, Etnia, Cabellos,Ojos, Seguidores, UsuarioArteGenero ,Intereses, InteresesUsuario, GeneroArtistico, TipoArte, SectorIndustria,Pais
from .models import *
from .forms import FormActualizarDatos, FormExperiencia, FormEducacion, FormMensaje
from core.UploadFile import UploadFile
from core.utils import getDatosActualizar
from frontend.funciones import form_invalid
from core.clases.ClassUsuario import Usuario
from django.db.models import Q
import json
from django.shortcuts import redirect
from datetime import date
from casting.models import Casting
from django.utils import formats
from django.utils.dateparse import parse_date


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
    return HttpResponse(json.dumps({'mensaje': str(_(']Cover cambiado exitosamente')), 'success': True}), content_type="application/json")



def Configuracion_Seguriad_Actualizar(request):
    if request.method == 'POST':
        cambiar_pass = False
        if len(request.POST['email']) > 0:
            User.objects.filter(uuid=request.user.uuid, email=request.POST['correo']).update(
                email=request.POST['email']
            )
        if len(request.POST['old_password']) > 0:
            form_pass = PasswordChangeForm(request.user, request.POST)
            if form_pass.is_valid():
                form = form_pass.save(commit=False)
                form.save()
            else:
                messages.add_message(request, messages.WARNING, form_pass.errors)

        return HttpResponse(json.dumps({'success':True}), content_type="application/json")

def Configuracion_Idioma_Actualizar(request):
    if request.method == 'POST':
        datos = getDatosActualizar(User, request)
        User.objects.filter(uuid=request.user.uuid).update(**datos)

        return HttpResponse(json.dumps({'mensaje': ''}), content_type="application/json")

def Agregar_Idioma(request):
    if request.method == 'POST':
        if UsuarioIdioma.objects.get(id_idioma=Idioma.objects.get(id=request.POST['id_idioma']), id_usuario=request.user) is None:
            UsuarioIdioma.objects.create(id_idioma=Idioma.objects.get(id=request.POST['id_idioma']), id_usuario=request.user)
            html=' <tr ><td>'
            html+=Idioma.objects.get(id=request.POST['id_idioma']).nombre
            html+= '</td><td><a href = "#">icono Editar</a></td> </tr>'
            return HttpResponse(json.dumps({'html':html,'mensaje': 'Idioma Agregado', 'success': True}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'mensaje': 'Ya existe este idioma en tu experiencia', 'success': False}), content_type="application/json")            

def Configuracion_Interes(request):
    if request.method == 'POST':
        total = len(Intereses.objects.all())
        for x in range(1,total+1):    
            #SI VIENE LA SOLICITUD       
            if 'interes-'+str(x) in request.POST:   
                
                #SI NO EXISTE, LA CREO
                if InteresesUsuario.objects.filter(id_interes=Intereses.objects.get(id=x),id_usuario=request.user).count() == 0:
                    InteresesUsuario.objects.create(id_interes=Intereses.objects.get(id=x),id_usuario=request.user)
            #SI NO VIENE LA SOLICITUD
            else:
                #SI EXISTE, ENTONCES LA ELIMINO
                if InteresesUsuario.objects.filter(id_interes=Intereses.objects.get(id=x),id_usuario=request.user).count() == 1:
                    InteresesUsuario.objects.filter(id_interes=Intereses.objects.get(id=x),id_usuario=request.user).delete()
       
        #import pdb; pdb.set_trace()
        #return HttpResponseRedirect('/perfil/configuraciongeneral/')
        return HttpResponse(json.dumps({'mensaje':'Intereses Modificados exitosamente','success':True}), content_type="application/json")    


def Configuracion_General_Actualizar(request):
    
   if request.method == 'POST':
        datos = getDatosActualizar(User, request)
        #
        user = User.objects.filter(uuid=request.user.uuid).update(**datos)     
       
        if 'tatuaje' in request.POST:           
            User.objects.filter(uuid=request.user.uuid).update(tatuaje=(request.POST['tatuaje'] == 'True'))

        if 'disponible_viajes' in request.POST:
            User.objects.filter(uuid=request.user.uuid).update(disponible_viajes=(request.POST['disponible_viajes'] == 'True'))
                
        #import pdb; pdb.set_trace()
        return HttpResponseRedirect('/perfil/configuraciongeneral/') 
        #return HttpResponse(json.dumps({'mensaje':'Datos guardados exitosamente','success':True}), content_type="application/json")    


def Configuracion_General(request):
    cabellos = Cabellos.objects.all()
    ojos = Ojos.objects.all()
    etnias = Etnia.objects.all()
    intereses = Intereses.objects.all()
    interesesusuario= InteresesUsuario.objects.filter(id_usuario=request.user).values_list('id_interes', flat=True)
    idiomas = Idioma.objects.all()
    data = User.objects.get(uuid=request.user.uuid)
    form_pass = PasswordChangeForm(request.user)
    form_pass.fields['old_password'].widget.attrs = {'required': 'required',
                                                'label': _('Contraseña actual')}
    form_pass.fields['new_password1'].widget.attrs = {'required': 'required',
                                                 'label': _('Nueva contraseña')}
    form_pass.fields['new_password2'].widget.attrs = {'required': 'required',
                                                 'label': _('Confirme su nueva contraseña')}
    idiomas_user = UsuarioIdioma.objects.filter(id_usuario=request.user.id)
    paises=Pais.objects.all()
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
        'cabellos':cabellos,
        'intereses':intereses,
        'interesesusuario':interesesusuario,
        'idiomas':idiomas,
        'idiomas_user':idiomas_user,
        'paises':paises
    }
    #import pdb; pdb.set_trace()
    return render(request, "perfiles/configuraciongeneral.html", context)

def ConfiguracionExperiencia(request):
    if request.method == 'POST':  
        if request.POST['id_experiencia'] == '':
            form = FormExperiencia(request.POST)
            if form.is_valid():
                experiencia = form.save(commit=False)
                experiencia.usuario = User.objects.get(uuid=request.POST['usuario'])
                if request.POST['fecha_hasta'] != '':
                    experiencia.fecha_hasta=request.POST['fecha_hasta']
                experiencia.save()
                xHTML="<tr><td>"+request.POST['empresa']+"</td>"
                xHTML+="<td>"+request.POST['cargo']+"</td>"
                xHTML+="<td>"+request.POST['fecha_desde']+" - "
                if request.POST['fecha_hasta'] == '':
                    xHTML+= "Actualidad</td>"
                else:                     
                    xHTML+=request.POST['fecha_hasta']+"</td>"
                if 'trabajo_actual' in request.POST:
                    xHTML+="<td>Si</td>"
                else:
                    xHTML+="<td>No</td>"  
                xHTML+='<td><a class="editar_experiencia" data-id='+str(experiencia.id)+"href=#><span class='glyphicon glyphicon-pencil'></span></a></td></tr>"   
                 
                return HttpResponse(json.dumps({'xHTML':xHTML,'success': True}), content_type="application/json")
            else:
                return HttpResponse(json.dumps(form_invalid(form)), content_type="application/json")
        else:
            #a=getDatosActualizar(Experiencia,request)
            #import pdb; pdb.set_trace()

            exp=Experiencia.objects.get(id=request.POST['id_experiencia'])
            exp.empresa=request.POST['empresa']
            exp.cargo=request.POST['cargo']
           
            exp.fecha_desde=request.POST['fecha_desde'].split('/')[2]+'-'+request.POST['fecha_desde'].split('/')[1]+'-'+request.POST['fecha_desde'].split('/')[0]
            if request.POST['fecha_hasta'] != '':                
                exp.fecha_hasta=request.POST['fecha_hasta']
            else:
                exp.fecha_hasta=None;

            if 'trabajo_actual' in request.POST:
                exp.trabajo_actual=True;
            else:
                exp.trabajo_actual=False;
            #exp.fecha_desde=request.POST['fecha_desde']
            exp.save()

            xHTML='<td>'+request.POST['empresa']+'</td>'
            xHTML+='<td>'+request.POST['cargo']+'</td>'
            xHTML+="<td>"+request.POST['fecha_desde']+" - "
            if request.POST['fecha_hasta'] == '':
                xHTML+= "Actualidad</td>"
            else:                     
                xHTML+=request.POST['fecha_hasta']+"</td>"
            if 'trabajo_actual' in request.POST:
                xHTML+="<td>Si</td>"
            else:
                xHTML+="<td>No</td>"  
            xHTML+='<td><a class="editar_experiencia" data-id='+request.POST['id_experiencia']+" href=#><span class='glyphicon glyphicon-pencil'></span></a></td>"
            return HttpResponse(json.dumps({'xHTML':xHTML,'success': True}), content_type="application/json")

def Buscar_Experiencia(request):
    if request.method == 'POST':
        exp= Experiencia.objects.get(id=request.POST['id'])
        #import pdb; pdb.set_trace()
        dia_hasta=''
        mes_hasta=''
        anno_hasta=''
        if exp.fecha_hasta:
            dia_hasta=exp.fecha_hasta.day
            mes_hasta=exp.fecha_hasta.month
            anno_hasta=exp.fecha_hasta.year

        context={'empresa':exp.empresa, 
                'cargo':exp.cargo,
                'dia_desde':exp.fecha_desde.day,
                'mes_desde':exp.fecha_desde.month,
                'anno_desde':exp.fecha_desde.year,
                'dia_hasta':dia_hasta,
                'mes_hasta':mes_hasta,
                'anno_hasta':anno_hasta,
                'success': True}

        
        return HttpResponse(json.dumps(context), content_type="application/json")

def Configuracion_Educacion(request):
    if request.method == 'POST':
        #import pdb; pdb.set_trace()
        if request.POST['id_educacion'] == '':
            form = FormEducacion(request.POST)
            
            if form.is_valid():
                educacion = form.save(commit=False)
                educacion.usuario = User.objects.get(uuid=request.POST['usuario'])
                if request.POST['fecha_fin_estudio'] != '':
                    educacion.fecha_fin_estudio=request.POST['fecha_fin_estudio']
                educacion.save()
                xHTML="<tr><td>"+request.POST['institucion']+"</td>"
                xHTML+="<td>"+request.POST['titulo']+"</td>"
                xHTML+="<td>"+request.POST['fecha_inicio_estudio']+" - "
                if request.POST['fecha_fin_estudio'] == '':
                    xHTML+= "Actualidad</td>"
                else:                     
                    xHTML+=request.POST['fecha_fin_estudio']+"</td>"
                if 'estudiando_actualmente' in request.POST:
                    xHTML+="<td>Si</td>"
                else:
                    xHTML+="<td>No</td>"
                xHTML+='<td><a class="editar_educacion" data-id='+str(educacion.id)+"href=#><span class='glyphicon glyphicon-pencil'></span></a></td></tr>"
                return HttpResponse(json.dumps({'xHTML':xHTML,'success': True}), content_type="application/json")
            else:
                return HttpResponse(json.dumps(form_invalid(form)), content_type="application/json")
        else:
            #a=getDatosActualizar(Experiencia,request)
            #import pdb; pdb.set_trace()
            print("editar_educacion")
            edu=Educacion.objects.get(id=request.POST['id_educacion'])
            edu.institucion=request.POST['institucion']
            edu.titulo=request.POST['titulo']
           
            edu.fecha_inicio_estudio=request.POST['fecha_inicio_estudio'].split('/')[2]+'-'+request.POST['fecha_inicio_estudio'].split('/')[1]+'-'+request.POST['fecha_inicio_estudio'].split('/')[0]
            if request.POST['fecha_fin_estudio'] != '':                
                edu.fecha_fin_estudio=request.POST['fecha_fin_estudio']
            else:
                edu.fecha_fin_estudio=None;

            if 'estudiando_actualmente' in request.POST:
                edu.estudiando_actualmente=True;
            else:
                edu.estudiando_actualmente=False;
            #edu.fecha_desde=request.POST['fecha_desde']
            edu.save()
            xHTML="<td>"+request.POST['institucion']+"</td>"
            xHTML+="<td>"+request.POST['titulo']+"</td>"
            xHTML+="<td>"+request.POST['fecha_inicio_estudio']+" - "
            if request.POST['fecha_fin_estudio'] == '':
                xHTML+= "Actualidad</td>"
            else:                     
                xHTML+=request.POST['fecha_fin_estudio']+"</td>"
            if 'estudiando_actualmente' in request.POST:
                xHTML+="<td>Si</td>"
            else:
                xHTML+="<td>No</td>"
            xHTML+='<td><a class="editar_educacion" data-id='+request.POST['id_educacion']+"href=#><span class='glyphicon glyphicon-pencil'></span></a></td></tr>"

          
            return HttpResponse(json.dumps({'xHTML':xHTML,'success': True}), content_type="application/json")

def Buscar_Educacion(request):
    if request.method == 'POST':
        print("Buscar_Educacion")
        edu= Educacion.objects.get(id=request.POST['id'])
        #import pdb; pdb.set_trace()
        dia_hasta=''
        mes_hasta=''
        anno_hasta=''
        if edu.fecha_fin_estudio:
            dia_hasta=edu.fecha_fin_estudio.day
            mes_hasta=edu.fecha_fin_estudio.month
            anno_hasta=edu.fecha_fin_estudio.year

        context={'institucion':edu.institucion, 
                'titulo':edu.titulo,
                'dia_desde':edu.fecha_inicio_estudio.day,
                'mes_desde':edu.fecha_inicio_estudio.month,
                'anno_desde':edu.fecha_inicio_estudio.year,
                'dia_hasta':dia_hasta,
                'mes_hasta':mes_hasta,
                'anno_hasta':anno_hasta,
                'success': True}

        #import pdb; pdb.set_trace()
        
        return HttpResponse(json.dumps(context), content_type="application/json")


def Perfil(request, uuid):
    usuario = Usuario(uuid)
    
    datos_personales = usuario.getDatosPersonales()
    seguir =len(Seguidores.objects.filter(destino=request.user))
    
   
    enviados = Mensaje.objects.filter(origen=request.user.id)
    recibidos = Mensaje.objects.filter(destino=request.user.id)
    interesesusuario = InteresesUsuario.objects.filter(id_usuario=datos_personales.id)
    castings=''
    edad=''
    profesion=''
    if datos_personales.tipo_usuario == 'I' or datos_personales.tipo_usuario == 'P' or datos_personales.tipo_usuario == 'F' :
        tema = 'azul'
        castings = Casting.objects.filter(autor=datos_personales.id).order_by('fecha_fin')[:2]
        profesion= SectorIndustria.objects.get(id_usuario=datos_personales.id)
    else:
        tema = 'naranja'
        edad = date.today().year-datos_personales.fecha_nacimiento.year
        profesion = UsuarioArteGenero.objects.get(id_usuario=datos_personales.id)

    context = {
        'datos_personales' : datos_personales,
        'educacion': usuario.getEducacion(),
        'experiencia' : usuario.getExperiencia(),
        'tema' : tema,
        'titulo': _('Perfil de usuario '),
        'usuario':usuario,
        'fans':seguir,
        'enviados':enviados,
        'recibidos':recibidos,
        'edad':edad,
        'interesesusuario':interesesusuario,
        'castings': castings,
        'profesion':profesion
    }
    #import pdb; pdb.set_trace()
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
        
        archivo_list = Multimedia.objects.filter(usuario=User.objects.get(uuid=request.META['HTTP_REFERER'].split('/')[4]), tipo_archivo=archivo)
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

def detalle_mensajes(request):
    #import pdb; pdb.set_trace()      
    if request.method == 'POST':
        mensaje = Mensaje.objects.get(id=request.POST['idmensaje'])
        #si es mensaje lo envie
        if mensaje.origen.id == request.user.id:
            destino = mensaje.destino.email
        else:
            destino = mensaje.origen.email
        imagen=''
        archivo=''
        if mensaje.imagen != '':
            imagen=mensaje.imagen.url

        if mensaje.archivo != '':
            archivo=mensaje.archivo.url
        
    return HttpResponse(json.dumps({'mensaje':'desde el ajax','destino':destino, 'mensaje':mensaje.mensaje,'imagen':imagen,'archivo':archivo,'success':True}), content_type="application/json")    


# OJO   OJO    OJO     OJO     OJO   OJO 
# NECESITO QUE SEA AJAX PARA PODER MANTENERME EN LA MISMA PAG¿INA
def enviar_mensajes(request):
    if request.method == 'POST':   
       
        mensaje=''
        form = FormMensaje(request.POST, request.FILES) 
        import pdb; pdb.set_trace()       
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
    return render(request,"seguidores/seguidores.html", {"seguidores": seguidores })


def siguiendo(request,uuid):

    lista = Seguidores.objects.filter(origen=User.objects.get(uuid=uuid)).values_list('destino', flat=True)
    talentos = User.objects.filter(id__in=lista, tipo_usuario='A').values_list('id', flat=True)
    industrias = User.objects.filter(id__in=lista, tipo_usuario='I').values_list('id', flat=True)
    usuarios = UsuarioArteGenero.objects.filter(id_usuario__in=talentos)
    industriass = SectorIndustria.objects.filter(id_usuario__in=industrias)
    #import pdb;   pdb.set_trace()
    paginator = Paginator(usuarios, 15)
    page = request.GET.get('page',1)
    try:
        seguidores = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        seguidores = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        seguidores = paginator.page(paginator.num_pages)
        
    return render(request,"seguidores/siguiendo.html", {"seguidores": seguidores , 'industriass':industriass})




