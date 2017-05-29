from django.shortcuts import render_to_response, render, redirect
from django.core.urlresolvers import reverse
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import  FormRegistro, FormAudicion
from frontend.models import User, SectorIndustria, Industria, UsuarioArteGenero
import json
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from frontend.funciones import form_invalid
from django.utils.translation import ugettext_lazy as _
from datetime import date


# Create your views here.
#LISTA GENERAL
def todos(request):
	
	categorias= Industria.objects.filter(tipo='I')
	all_casting = Casting.objects.all().order_by("fecha_fin")
	paginator = Paginator(all_casting, 10) # Show 25 contacts per page
	page = request.GET.get('page',1)
	try:
		castings = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		castings = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		castings = paginator.page(paginator.num_pages)
		#import pdb;   pdb.set_trace()
	#import pdb;   pdb.set_trace()
	return render(request, "casting/inicio.html", {"castings": castings, "categorias":categorias })

#LISTADO POR CATEGORIA
def casting_por_categoria(request, idcategoria):
	categorias= Industria.objects.all()
	#import pdb; pdb.set_trace()
	categoria = Industria.objects.get(id=idcategoria)

	all_casting = categoria.casting_set.order_by("fecha_fin")
	paginator = Paginator(all_casting, 10) # Show 25 contacts per page	
	page = request.GET.get('page',1)
	try:
		castings = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		castings = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		castings = paginator.page(paginator.num_pages)
	#import pdb;   pdb.set_trace()
	return render(request, "casting/inicio.html", {"castings": castings,"categorias":categorias })

#DETALLES DE UN CASTING
def detalle(request,idcasting):

	casting = Casting.objects.get(id=idcasting)
	asociados= Casting.objects.filter(autor=casting.autor).exclude(id=idcasting)[:2]
	#import pdb;   pdb.set_trace()
	return render(request,"casting/detalle.html", {"casting": casting, "asociados": asociados },)


#def crear(request):
#	return render_to_response("casting/crear.html",{},)

#CREACION DE UN CASTING
def crear(request):	

	if request.user.tipo_usuario == 'I':
		categorias=Industria.objects.filter(tipo='I')
		if request.method == 'POST':	
			#import pdb; pdb.set_trace()		
			mensaje = ''
			error = ''
			form = FormRegistro(request.POST, request.FILES)
			if form.is_valid():
				#import pdb;   pdb.set_trace()
				casting = form.save(commit=False)
				casting.autor = User.objects.get(email=request.user.email)					
				casting.save()	
				success = True	
				#context = {'from': FormRegistro, "categorias":categorias }
				mensaje = {'mensaje': str(_('Casting creado con exito')), 'success': True}		
				messages.success(request, 'Casting creado con exito')
			else:
				mensaje = form_invalid(form)
				success = False
				messages.success(request, 'No pudo ser creado')
				#REVISAR ESTE RETURN DEL MENSAJE... SE MUESTRA EL JSON Y NO UN MENSAJE "REGULAR"
				#return HttpResponse(json.dumps(mensaje), content_type="application/json")
		#
		context = {'from': FormRegistro, "categorias":categorias }
		return render(request, "casting/crear.html", context)
	else:
		return HttpResponseRedirect( "/",{})	

#COMO QUE NO HACE NADA PORQUE LO QUE PENSABA HACER, LO RESOLVI CON EL MESSAGE DE LA FUNCION ANTERIOR
def guardar(request):
    if request.method == 'POST':
        form = FormRegistro(request.POST)
        if form.is_valid():
            casting = form.save(commit=False)
            casting.autor = User.objects.get(uuid=request.user.uuid)
            casting.save()
            #return HttpResponse(json.dumps({'success': True}), content_type="application/json")
        #else:
            #return HttpResponse(json.dumps(form_invalid(form)), content_type="application/json")
    return HttpResponseRedirect('/casting/inicio/')


def audicion1(request, casting):
	if request.user.tipo_usuario == 'A':
		#categorias=Categoria.objects.all()
		if request.method == 'POST':			
			mensaje = ''
			error = ''
			form = FormAudicion(request.POST, request.FILES)
			if form.is_valid():
				#import pdb;   pdb.set_trace()
				audicion = form.save(commit=False)
				audicion.id_usuario = User.objects.get(email=request.user.email)
				audicion.id_casting = Casting.objects.get(id=casting)					
				audicion.save()		
				mensaje = {'mensaje': str(_('Audicion creada con exito')), 'success': True}	
				messages.success(request, 'Audicion creada con exito')	
				#ver como devuelvo estatus correcto print('bueeeno')
			else:
				#	ESTA DEVOLVIENDO ESTO, PERO NI IDEA DE POR QUE
				mensaje = form_invalid(form)
				messages.warning(request, 'Audicion creada con exito')
				#ver como devuelvo estatus incorrecto print("maaalo")			
			return redirect(reverse("casting:casting_detalle", args=[casting]))
			
		context = {'from': FormAudicion,'casting':casting }
		return render(request,'casting/audicion-1.html',context)
	else:
		return HttpResponseRedirect( "/",{})

#PANEL DE ADMINISTRACION DE AUDICIONES
def panel (request):
	castings = Casting.objects.filter(fecha_fin__gte=date.today()).order_by("fecha_fin")[:6]
	fincastings = Casting.objects.filter(autor=request.user, fecha_fin__lt=date.today())
	usercastings = Casting.objects.filter(autor=request.user,fecha_fin__gte=date.today()).order_by("fecha_fin")[:6]
	proveedores = SectorIndustria.objects.filter(id_sector=Industria.objects.filter(tipo='P'))[:4]
	#import pdb; pdb.set_trace()
	return render(request, 'casting/castingpanel.html',{'proveedores':proveedores,'castings':castings, 'usercastings':usercastings,'fincastings':fincastings})

#MUESTRA  EL CASTING Y SU AUDICIONES
def casting_ind(request,idcasting):
	casting = Casting.objects.get(id=idcasting)
	audiciones = Audicion.objects.filter(id_casting=idcasting)

	if casting.imagen_1:
		imagen= casting.imagen_1.url
	else:
		imagen=''
	audi=''
	ganador=''
	for audicion in audiciones:
		if audicion.ganador:
			usuario_ganador= UsuarioArteGenero.objects.get(id_usuario=audicion.id_usuario)
			ganador = '<div class="col-md-12 ivo-mensaje-contenido ivo-mensaje-contenido-audicion ivo-casting-ganador-top">'
			ganador+='<div class="row">'
			ganador+='<div class="col-md-12 ivo-casting-ganador ivo-borde-azulClaro">'
			ganador+='<div class="row">'
			ganador+='<div class="col-md-3 ivo-casting-ganador-imagen" style="background:url('+usuario_ganador.id_usuario.avatar.url+')">'
			ganador+='<a href="#" class="ivo-back-azulClaro elemento_audicion" data-audicion="'+str(audicion.id)+'">Ver Audicion</a>'
			ganador+='</div>'
			ganador+='<div class="col-md-4 ivo-artistas-panel-item ivo-casting-ganador-info">'
			ganador+='<div class="ivo-casting-ganador-titulo">Ganador</div>'
			ganador+='<h3 class="ivo-font-negro">'+usuario_ganador.id_genero.id_tipo_arte.name+'</h3>'
			ganador+='<h4 class="ivo-font-negro"><b>'+usuario_ganador.id_usuario.get_full_name()+'</b></h4>'
			ganador+='<h4 class="ivo-font-negro">'+usuario_ganador.id_genero.name+'</h4>'
			ganador+='</div>'
			ganador+='<div class="col-md-4">'
			ganador+='<ul class="ivo-dashboard-infoBasica ivo-perfil-info ivo-casting-ganador-fans">'
			ganador+='<li style="margin-bottom: 5px !important;">'
			ganador+='<span class="glyphicon glyphicon-heart ivo-font-naranja"></span><i><b>500 fans</b></i>'
			ganador+='</li>'
			ganador+='<li>'
			ganador+='<span class="glyphicon glyphicon-star ivo-font-naranja"></span>'
			ganador+='<span class="glyphicon glyphicon-star ivo-font-naranja"></span>'
			ganador+='<span class="glyphicon glyphicon-star ivo-font-naranja"></span>'
			ganador+='<span class="glyphicon glyphicon-star ivo-font-naranja"></span>'
			ganador+='<span class="glyphicon glyphicon-star-empty ivo-font-naranja"></span>'
			ganador+='</li>'
			ganador+='<li><a href="/perfil/'+usuario_ganador.id_usuario.uuid+'/" class="ivo-font-azulClaro"><i><b>Ver Perfil</b></i></a></li>'
			ganador+='</ul>'
			ganador+='</div>'
			ganador+='<div class="col-md-1">'
			ganador+='<img class="ivo-mensajes-trofeo ivo-ganador-trofeo" src="/static/img/trofeo.png" >'
			ganador+='</div>'
			ganador+='</div>'
			ganador+='</div>'
			ganador+='</div>'
			ganador+='</div>'
		
		audi+='	<li class="row elemento_audicion" data-audicion="'+str(audicion.id)+'" ><div class="col-md-2" > '
		if audicion.id_usuario.avatar is not None:
			audi+=' <img class="img-responsive " src="'+audicion.id_usuario.avatar.url+'">'
		else:
			audi+= '<img class="img-responsive" src="cualquier/foto.jpg">'
															
		audi += '</div><div class="col-md-7" ><span class="ivo-etiqueta-titulo ivo-font-verde ivo-dashboard-etq ">'+audicion.id_usuario.get_full_name()+'</span></div></li>'
		

	#import pdb; pdb.set_trace()
	if casting is not None:
		return HttpResponse(json.dumps({'ganador':ganador,'audiciones':audi,'id':idcasting,'img': imagen, 'dia_fin': str(casting.fecha_fin.day),'mes_fin': str(casting.fecha_fin.month),'anno_fin': str(casting.fecha_fin.year),'descripcion':casting.descripcion ,'titulo':casting.titulo,'mensaje': str(_('Casting Encontrado')), 'success': True}), content_type="application/json")
	else:
		return HttpResponse(json.dumps({'mensaje': str(_('Casting NO Encontrado')), 'success': False}), content_type="application/json")



#MUESTRA LA AUDICION
def casting_aud(request,idaudicion):
	
	
	audicion = Audicion.objects.get(id=idaudicion)
	#import pdb; pdb.set_trace()
	#audi=''
	if audicion.archivo:
		if audicion.archivo.name.endswith('.jpg') or audicion.archivo.name.endswith('.png'):
			audi = ' <div class="row"><div class="col-md-12 ivo-mensaje-contenido ivo-mensaje-contenido-audicion"><img src="'
			audi += audicion.archivo.url
			audi += '" class="img-responsive ivo-mensaje-img">'
		# else:
		# 	audi = ' <div class="row"><div class="col-md-12 ivo-mensaje-contenido ivo-mensaje-contenido-audicion"><img src="'
		# 	audi += 'cualquier_imagen.jpg'
		elif audicion.archivo.name.endswith('.mp3'):
			audi = '<div class="row"><div class="col-md-12 ivo-mensaje-contenido ivo-mensaje-contenido-audicion">'
			audi += '<div class="ivo-mensaje-contenedorAudio ivo-mensaje-contenedorAudio-noBorde ivo-contenedorAudio-bck1">'
			audi += '<div class="ivo-mensaje-contenedorAudio-carga" id = "progreso_audio-1" style="width: 0%;"></div>'
			audi += '<div class="ivo-mensaje-contenedorAudio-contenido">'
			audi += '<div>'
			audi += '<span class="arrow_triangle-right_alt ivo-font-naranja play_audio" id = "1" audio = "' + audicion.archivo.url + '"></span>'
			audi += '</div>'
			audi += '<h5>'+audicion.archivo.name.split('/')[1]+'</h5>'
			audi += '</div>'
			audi += '<div class="ivo-mensaje-contenedorAudio-contenido2">'
			audi += '<span class="tiempo" id = "tiempo_audio-1">00:00</span>'
			audi += '</div>'
			audi += '</div>'
			audi += '</div>'

	#import pdb; pdb.set_trace()

	audi +='<h2>PORQUE PARTICIPAS EN ESTE CASTING</h2><p>'+audicion.motivo_participar+'</p><h2>CUENTANOS UN POCO MAS DE TI</h2><p>'+audicion.cuentanos+'</p>'
	audi += '</div></div><div class="row"><div class="col-md-12 text-right">'
	audi += '<a class="ivo-boton" id="boton_ganador" href="#" data-audicion="'+str(audicion.id)+'">Ganador</a><a class="ivo-boton" href="#">Ver Casting</a>'
	audi += '<a class="ivo-boton" href="#">Eliminar</a></div></div>'	

	return HttpResponse(json.dumps({'audiciones':audi,'mensaje': str(_('Casting Encontrado')), 'success': True}), content_type="application/json")
	

#GUARDA EL GANADOR DEL CASTING
def casting_ganador(request):
	if request.method=='POST':
		audicion=Audicion.objects.get(id=request.POST['idaudicion'])
		ganador_actual= Audicion.objects.get(id_casting=audicion.id_casting, ganador=True)
		ganador_actual.ganador= not ganador_actual.ganador
		audicion.ganador= not audicion.ganador
		ganador_actual.save()
		audicion.save()
		#import pdb; pdb.set_trace()
		return HttpResponse(json.dumps({'mensaje': str(_('Definido nuevo ganador')), 'success': True}), content_type="application/json")

