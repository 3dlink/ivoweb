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
from django.db.models import Q
from django.core.mail import send_mail, BadHeaderError


# Create your views here.
#LISTA GENERAL
def todos(request):
	if request.user.tipo_usuario == 'A':
		categorias= TipoArte.objects.all()

		filtro_1 = Q(publico=True)
		filtro_2 = Q(pais=request.user.pais.id) & Q(color_cabello=None) & Q(color_ojos=None) & Q(tatuaje='') & Q(etnia=None) & Q(publico=False)
		filtro_3 = Q(pais=None) & Q(color_cabello=request.user.color_cabello.id) & Q(color_ojos=None) & Q(tatuaje='') & Q(etnia=None) & Q(publico=False)
		filtro_4 = Q(pais=request.user.pais.id) & Q(color_cabello=request.user.color_cabello.id) & Q(color_ojos=None) & Q(tatuaje='') & Q(etnia=None) & Q(publico=False)
		filtro_5 = Q(pais=None) & Q(color_cabello=None) & Q(color_ojos=request.user.color_ojos.id) & Q(tatuaje='') & Q(etnia=None) & Q(publico=False)
		filtro_6 = Q(pais=request.user.pais.id) & Q(color_cabello=None) & Q(color_ojos=request.user.color_ojos.id) & Q(tatuaje='') & Q(etnia=None) & Q(publico=False)
		filtro_7 = Q(pais=None) & Q(color_cabello=request.user.color_cabello.id) & Q(color_ojos=request.user.color_ojos.id) & Q(tatuaje='') & Q(etnia=None) & Q(publico=False)
		filtro_8 = Q(pais=request.user.pais.id) & Q(color_cabello=request.user.color_cabello.id) & Q(color_ojos=request.user.color_ojos.id) & Q(tatuaje='') & Q(etnia=None) & Q(publico=False)
		filtro_9 = Q(pais=None) & Q(color_cabello=None) & Q(color_ojos=None) & Q(tatuaje=request.user.tatuaje) & Q(etnia=None) & Q(publico=False)
		filtro_10 = Q(pais=request.user.pais.id) & Q(color_cabello=None) & Q(color_ojos=None) & Q(tatuaje=request.user.tatuaje) & Q(etnia=None) & Q(publico=False)
		filtro_11 = Q(pais=None) & Q(color_cabello=request.user.color_cabello.id) & Q(color_ojos=None) & Q(tatuaje=request.user.tatuaje) & Q(etnia=None) & Q(publico=False)
		filtro_12 = Q(pais=request.user.pais.id) & Q(color_cabello=request.user.color_cabello.id) & Q(color_ojos=None) & Q(tatuaje=request.user.tatuaje) & Q(etnia=None) & Q(publico=False)
		filtro_13 = Q(pais=None) & Q(color_cabello=None) & Q(color_ojos=request.user.color_ojos.id) & Q(tatuaje=request.user.tatuaje) & Q(etnia=None) & Q(publico=False)
		filtro_14 = Q(pais=request.user.pais.id) & Q(color_cabello=None) & Q(color_ojos=request.user.color_ojos.id) & Q(tatuaje=request.user.tatuaje) & Q(etnia=None) & Q(publico=False)
		filtro_15 = Q(pais=None) & Q(color_cabello=request.user.color_cabello.id) & Q(color_ojos=request.user.color_ojos.id) & Q(tatuaje=request.user.tatuaje) & Q(etnia=None) & Q(publico=False)
		filtro_16 = Q(pais=request.user.pais.id) & Q(color_cabello=request.user.color_cabello.id) & Q(color_ojos=request.user.color_ojos.id) & Q(tatuaje=request.user.tatuaje) & Q(etnia=None) & Q(publico=False)
		filtro_17 = Q(pais=None) & Q(color_cabello=None) & Q(color_ojos=None) & Q(tatuaje='') & Q(etnia=request.user.etnia.id) & Q(publico=False)
		filtro_18 = Q(pais=request.user.pais.id) & Q(color_cabello=None) & Q(color_ojos=None) & Q(tatuaje='') & Q(etnia=request.user.etnia.id) & Q(publico=False)
		filtro_19 = Q(pais=None) & Q(color_cabello=request.user.color_cabello.id) & Q(color_ojos=None) & Q(tatuaje='') & Q(etnia=request.user.etnia.id) & Q(publico=False)
		filtro_20 = Q(pais=request.user.pais.id) & Q(color_cabello=request.user.color_cabello.id) & Q(color_ojos=None) & Q(tatuaje='') & Q(etnia=request.user.etnia.id) & Q(publico=False)
		filtro_21 = Q(pais=None) & Q(color_cabello=None) & Q(color_ojos=request.user.color_ojos.id) & Q(tatuaje='') & Q(etnia=request.user.etnia.id) & Q(publico=False)
		filtro_22 = Q(pais=request.user.pais.id) & Q(color_cabello=None) & Q(color_ojos=request.user.color_ojos.id) & Q(tatuaje='') & Q(etnia=request.user.etnia.id) & Q(publico=False)
		filtro_23 = Q(pais=None) & Q(color_cabello=request.user.color_cabello.id) & Q(color_ojos=request.user.color_ojos.id) & Q(tatuaje='') & Q(etnia=request.user.etnia.id) & Q(publico=False)
		filtro_24 = Q(pais=request.user.pais.id) & Q(color_cabello=request.user.color_cabello.id) & Q(color_ojos=request.user.color_ojos.id) & Q(tatuaje='') & Q(etnia=request.user.etnia.id) & Q(publico=False)
		filtro_25 = Q(pais=None) & Q(color_cabello=None) & Q(color_ojos=None) & Q(tatuaje=request.user.tatuaje) & Q(etnia=request.user.etnia.id) & Q(publico=False)
		filtro_26 = Q(pais=request.user.pais.id) & Q(color_cabello=None) & Q(color_ojos=None) & Q(tatuaje=request.user.tatuaje) & Q(etnia=request.user.etnia.id) & Q(publico=False)
		filtro_27 = Q(pais=None) & Q(color_cabello=request.user.color_cabello.id) & Q(color_ojos=None) & Q(tatuaje=request.user.tatuaje) & Q(etnia=request.user.etnia.id) & Q(publico=False)
		filtro_28 = Q(pais=request.user.pais.id) & Q(color_cabello=request.user.color_cabello.id) & Q(color_ojos=None) & Q(tatuaje=request.user.tatuaje) & Q(etnia=request.user.etnia.id) & Q(publico=False)
		filtro_29 = Q(pais=None) & Q(color_cabello=None) & Q(color_ojos=request.user.color_ojos.id) & Q(tatuaje=request.user.tatuaje) & Q(etnia=request.user.etnia.id) & Q(publico=False)
		filtro_30 = Q(pais=request.user.pais.id) & Q(color_cabello=None) & Q(color_ojos=request.user.color_ojos.id) & Q(tatuaje=request.user.tatuaje) & Q(etnia=request.user.etnia.id) & Q(publico=False)
		filtro_31 = Q(pais=None) & Q(color_cabello=request.user.color_cabello.id) & Q(color_ojos=request.user.color_ojos.id) & Q(tatuaje=request.user.tatuaje) & Q(etnia=request.user.etnia.id)	 & Q(publico=False)
		filtro_32 = Q(pais=request.user.pais.id) & Q(color_cabello=request.user.color_cabello.id) & Q(color_ojos=request.user.color_ojos.id) & Q(tatuaje=request.user.tatuaje) & Q(etnia=request.user.etnia.id)  & Q(publico=False)
		filtro =  filtro_2 | filtro_3 | filtro_4 | filtro_5 | filtro_6 | filtro_7 | filtro_8 | filtro_9 | filtro_10 | filtro_11 | filtro_12 | filtro_13 | filtro_4 | filtro_15 | filtro_16 | filtro_17 | filtro_18 | filtro_19 | filtro_20 | filtro_21 | filtro_22 | filtro_23 | filtro_24 | filtro_25 | filtro_26 | filtro_27 | filtro_28 | filtro_29 | filtro_30 | filtro_31 | filtro_32

		#buscar talentos en Tabla_Filtro
		filtro_genero = Q()
		for portalento in Filtro.objects.filter(id_talento=GeneroArtistico.objects.get(id=UsuarioArteGenero.objects.get(id_usuario=request.user).id_genero.id).id_tipo_arte.id):
			for porgenero in portalento.id_generos.all():
				if UsuarioArteGenero.objects.get(id_usuario=request.user).id_genero == porgenero:
					filtro_genero.add(Q(id=portalento.id_casting.id),Q.OR)

		
		all_casting = Casting.objects.filter((filtro & filtro_genero)|filtro_1).order_by("fecha_fin")
		all_casting = all_casting.filter(fecha_fin__gte=date.today())
		
		#import pdb; pdb.set_trace()
		paginator = Paginator(all_casting, 10) 
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
	elif request.user.tipo_usuario == 'I' or request.user.tipo_usuario == 'P':
		all_casting = Casting.objects.filter(fecha_fin__gte=date.today())
		categorias = TipoArte.objects.all()

		paginator = Paginator(all_casting, 10) 
		page = request.GET.get('page',1)
		try:
			castings = paginator.page(page)
		except PageNotAnInteger:
	        # If page is not an integer, deliver first page.
			castings = paginator.page(1)
		except EmptyPage:
	        # If page is out of range (e.g. 9999), deliver last page of results.
			castings = paginator.page(paginator.num_pages)
		return render(request, "casting/inicio.html", {"castings": castings, "categorias":categorias })
	else:
		return HttpResponseRedirect( "/",{})


#LISTADO POR CATEGORIA
def casting_por_categoria(request, idcategoria):
	categorias= TipoArte.objects.all()
	#import pdb; pdb.set_trace()
	categoria = Filtro.objects.filter(id_talento=idcategoria).values_list('id_casting',flat=True)

	all_casting = Casting.objects.filter(id__in=categoria,fecha_fin__gte=date.today())
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
		colores_ojos = Ojos.objects.all()
		colores_cabellos = Cabellos.objects.all()
		etnias= Etnia.objects.all()
		paises = Pais.objects.all().order_by('nombre')
		artes = TipoArte.objects.all()
		generos = GeneroArtistico.objects.all()

		if request.method == 'POST':	
			
			mensaje = ''
			error = ''
			form = FormRegistro(request.POST, request.FILES)
			if form.is_valid():
				#import pdb;   pdb.set_trace()
				casting = form.save(commit=False)
				casting.autor = User.objects.get(email=request.user.email)	
				if request.POST['tatuaje'] == 'True':
					casting.tatuaje=True
				elif request.POST['tatuaje']=='False':
					casting.tatuaje=False
				
				if request.POST['publico']=='False':
					casting.publico=False
				#borrar esto, solo validar el item 'Publico'
				# if request.POST['etnia']!='' or request.POST['color_cabello']!='' or request.POST['color_ojos']!='' or request.POST['pais']!='' or request.POST['tatuaje']!='':
				# 	casting.publico = False			
				casting.save()	
				
				
				#CREO O AGREGO ELEMENTOS DE A TABLA FILTRO
				for key in request.POST.keys():
					if key.split('-')[0] == 'genero':						
						obj, created = Filtro.objects.get_or_create(id_talento=GeneroArtistico.objects.get(id=key.split('-')[2]).id_tipo_arte, id_casting=casting)
						obj.id_generos.add(GeneroArtistico.objects.get(id=key.split('-')[2]))
							

				success = True	
				
				#A ESTOS SE LES MANDA EL CORREO
				
				filtro_correo= Q()
				for var_x in Filtro.objects.filter(id_casting=casting.id):
					for var_y in var_x.id_generos.all():
						filtro_correo.add(Q(id_genero=var_y.id),Q.OR)
						
				correos = UsuarioArteGenero.objects.filter(filtro_correo)

######  FILTROS POR USUARIO   #############
				
				f = Q()

				if request.POST['tatuaje']=='True':
					f.add(Q(tatuaje=True), Q.AND)
				elif request.POST['tatuaje']=='False':
					f.add(Q(tatuaje=False), Q.AND)

				if request.POST['etnia']!='':
					f.add(Q(etnia = Etnia.objects.get(id=request.POST['etnia']).id), Q.AND)
					
				if request.POST['color_ojos']!='':
					f.add(Q(color_ojos=Ojos.objects.get(id=request.POST['color_ojos']).id), Q.AND)
					
				if request.POST['color_cabello']!='':
					f.add(Q(color_cabello=Cabellos.objects.get(id=request.POST['color_cabello']).id), Q.AND)
					
				if request.POST['pais']!='':
					f.add(Q(pais=Pais.objects.get(id=request.POST['pais']).id), Q.AND)	
				
				

				
				usuarios = User.objects.filter(f).values_list('id',flat=True)
				correos = correos.filter(id_usuario__in=usuarios)
				#CON ESTA LISTA DE CORREOS, PUEDO ITERAR Y ENVIAR LOS DIFERENTES CORREOS
				#import pdb; pdb.set_trace()
				for element in correos:
					try:
						send_mail("Nuevo Casting en IvoTalents",element.id_usuario.first_name +' '+element.id_usuario.last_name +'\n\n  Se ha creado un casting que se ajusta a tus caracteristicas \n\n  Revisalo aqui: http://ivotalents.serveblog.net/casting/id/'+casting.id, 'correo@ivotalents.com', [str(element.id_usuario.email),'ati2mortiz@gmail.com'])
					except BadHeaderError:
						pass
				

				mensaje = {'mensaje': str(_('Casting creado con exito')), 'success': True}		
				messages.success(request, 'Casting creado con exito')
			else:
				mensaje = form_invalid(form)
				success = False
				messages.success(request, 'No pudo ser creado')
				
		context = {'artes':artes, 'generos':generos, 'from': FormRegistro, "categorias":categorias,"color_ojos":colores_ojos, "color_cabello":colores_cabellos,"etnias":etnias, "paises":paises }
		return render(request, "casting/crear.html", context)
	else:
		return HttpResponseRedirect( "/",{})	


def config_casting(request,idcasting):
	
	casting=Casting.objects.get(id=idcasting)
	filtros=Filtro.objects.filter(id_casting=idcasting)	
	colores_ojos = Ojos.objects.all()
	colores_cabellos = Cabellos.objects.all()
	etnias= Etnia.objects.all()
	paises = Pais.objects.all()
	artes = TipoArte.objects.all()
	generos = GeneroArtistico.objects.all()
	#import pdb; pdb.set_trace()
	return render(request, 'casting/editar_1.html',{'casting':casting,'filtros':filtros,"color_ojos":colores_ojos, "color_cabellos":colores_cabellos,"etnias":etnias, "paises":paises, 'artes':artes, 'generos':generos})


def editar_casting(request,idcasting):
	if request.user.tipo_usuario == 'I':
	
		
		if request.method=='POST':
			#import pdb; pdb.set_trace()
			Casting.objects.filter(id=idcasting).update(titulo=request.POST['titulo'], info_destacada=request.POST['info_destacada'],info_adicional=request.POST['info_adicional'],descripcion=request.POST['descripcion'], fecha_fin=request.POST['fecha_fin'],fecha_inicio=request.POST['fecha_inicio'],pais=request.POST['pais'], color_cabello=request.POST['color_cabello'],color_ojos=request.POST['color_ojos'],etnia=request.POST['etnia'] )
			casting = Casting.objects.get(id=idcasting)
			if request.POST['tatuaje'] == 'True':
				casting.tatuaje=True
			elif request.POST['tatuaje']=='False':
				casting.tatuaje=False
			else:
				casting.tatuaje=None

			if request.POST['publico']=='True':
				casting.publico=True
			else:
				casting.publico=False

			Filtro.objects.filter(id_casting=idcasting).delete()
			for key in request.POST.keys():
				if key.split('-')[0] == 'genero':						
					obj, created = Filtro.objects.get_or_create(id_talento=GeneroArtistico.objects.get(id=key.split('-')[2]).id_tipo_arte, id_casting=casting)
					obj.id_generos.add(GeneroArtistico.objects.get(id=key.split('-')[2]))
					casting.publico = False	

			casting.save()		

	return HttpResponse(json.dumps({'mensaje':'casting editado','casting':casting.id,'success': True}), content_type="application/json")

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
				messages.warning(request, 'Audicion no pudo ser creada')
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
		elif audicion.archivo.name.endswith('.mp4') or audicion.archivo.name.endswith('.ogg'):
			audi = ' <div class="row"><div class="col-md-12 ivo-mensaje-contenido ivo-mensaje-contenido-audicion"><video width="300px" height="300px" controls><source src="'
			audi += audicion.archivo.url
			audi += '"> </video>'
		# else:

	#import pdb; pdb.set_trace()

	audi +='<h2>PORQUE PARTICIPAS EN ESTE CASTING</h2><p>'+audicion.motivo_participar+'</p><h2>CUENTANOS UN POCO MAS DE TI</h2><p>'+audicion.cuentanos+'</p>'
	audi += '</div></div><div class="row"><div class="col-md-12 text-right">'
		

	if request.user.tipo_usuario=='I':
		if audicion.ganador == True:
			audi += '<a style="margin: 2px;" class="ivo-boton boton_ganador" id="boton_ganador" href="#" data-audicion="'+str(audicion.id)+'">Ganador Actual</a><a style="margin: 2px;" class="ivo-boton" href="/casting/id/'+str(audicion.id_casting.id)+'/">Ver Casting</a>'
		else:
			audi += '<a style="margin: 2px;" class="ivo-boton" id="boton_ganador" href="#" data-audicion="'+str(audicion.id)+'">Marcar Ganador</a><a style="margin: 2px;" class="ivo-boton" href="/casting/id/'+str(audicion.id_casting.id)+'/">Ver Casting</a>'
		audi += '<a style="margin: 2px;" class="ivo-boton" href="#">Eliminar</a></div></div>'
		return HttpResponse(json.dumps({'audiciones':audi,'mensaje': str(_('Casting Encontrado')), 'success': True}), content_type="application/json")
	elif request.user.tipo_usuario=='A':
		audi += '<a style="margin: 2px;" class="ivo-boton" href="/casting/id/'+str(audicion.id_casting.id)+'/">Ver Casting</a>'
		audi += '<a style="margin: 2px;" class="ivo-boton" href="/casting/borrar/audicion/'+str(audicion.id)+'/">Eliminar</a></div></div>'
		if audicion.id_casting.autor.avatar:
			imagen= audicion.id_casting.autor.avatar.url
		else:
			imagen=''
			#import pdb; pdb.set_trace()
		return HttpResponse(json.dumps({'img': imagen, 'dia_fin': str(audicion.id_casting.fecha_fin.day),'mes_fin': str(audicion.id_casting.fecha_fin.month),'anno_fin': str(audicion.id_casting.fecha_fin.year),'descripcion':audicion.id_casting.descripcion ,'titulo':audicion.id_casting.titulo,'mensaje': str(_('Casting Encontrado')), 'success': True,'audiciones':audi}), content_type="application/json")

#GUARDA EL GANADOR DEL CASTING
def casting_ganador(request):
	if request.method=='POST':
		audicion=Audicion.objects.get(id=request.POST['idaudicion'])
		ganador_actual= Audicion.objects.filter(id_casting=audicion.id_casting, ganador=True)
		if len(ganador_actual)==1:
			ganador_actual[0].ganador= not ganador_actual[0].ganador
			ganador_actual[0].save()
		audicion.ganador= not audicion.ganador
		audicion.save()

		if audicion.ganador == True:
			mensaje='Definido Nuevo Ganador'
		else:
			mensaje='Ganador eliminado'
		#import pdb; pdb.set_trace()
		return HttpResponse(json.dumps({'mensaje': mensaje, 'success': True}), content_type="application/json")


def borrar_casting(request, idcasting):
	Casting.objects.get(id=idcasting).delete()
	return redirect(reverse("casting:panel"))

def borrar_audicion(request, idaudicion):
	Audicion.objects.get(id=idaudicion).delete()
	return redirect(reverse("casting:audicionpanel"))


def audicionpanel (request):
	audiciones = Audicion.objects.filter(id_usuario=request.user)
	audicionesfin = Audicion.objects.filter(id_usuario=request.user, ganador=True)
	usercastings = Casting.objects.filter(autor=request.user,fecha_fin__gte=date.today()).order_by("fecha_fin")[:6]
	proveedores = SectorIndustria.objects.filter(id_sector=Industria.objects.filter(tipo='P'))[:4]
	#import pdb; pdb.set_trace()
	return render(request, 'casting/audicionpanel.html',{'proveedores':proveedores,'audiciones':audiciones, 'usercastings':usercastings,'audicionesfin':audicionesfin})

