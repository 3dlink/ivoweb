from django.shortcuts import render_to_response, render
from .models import Casting, Categoria
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import  FormRegistro, FormAudicion
from frontend.models import User
import json
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from frontend.funciones import form_invalid
from django.utils.translation import ugettext_lazy as _
from datetime import date


# Create your views here.
def todos(request):
	
	categorias= Categoria.objects.all()
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

def casting_por_categoria(request, idcategoria):
	categorias= Categoria.objects.all()
	import pdb; pdb.set_trace()
	categoria = Categoria.objects.get(nombre=idcategoria.replace("-"," "))

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
	import pdb;   pdb.set_trace()
	return render(request, "casting/inicio.html", {"castings": castings,"categorias":categorias })

def detalle(request,idcasting):

	casting = Casting.objects.get(id=idcasting)
	asociados= Casting.objects.filter(autor=casting.autor).exclude(id=idcasting)[:2]
	#import pdb;   pdb.set_trace()
	return render(request,"casting/detalle.html", {"casting": casting, "asociados": asociados },)


#def crear(request):
#	return render_to_response("casting/crear.html",{},)

def crear(request):	

	if request.user.tipo_usuario == 'I':
		categorias=Categoria.objects.all()
		if request.method == 'POST':			
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
		#import pdb; pdb.set_trace()
		context = {'from': FormRegistro, "categorias":categorias }
		return render(request, "casting/crear.html", context)
	else:
		return HttpResponseRedirect( "/",{})	

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
			else:
				mensaje = form_invalid(form)
				#REVISAR ESTE RETURN DEL MENSAJE... SE MUESTRA EL JSON Y NO UN MENSAJE "REGULAR"
			return HttpResponse(json.dumps(mensaje), content_type="application/json")
		context = {'from': FormAudicion,'casting':casting }
		return render(request,'casting/audicion-1.html',context)
	else:
		return HttpResponseRedirect( "/",{})

	
def panel (request):
	castings = Casting.objects.all().order_by("fecha_fin")[:6]
	fincastings = Casting.objects.filter(autor=request.user, fecha_fin__lt=date.today())
	usercastings = Casting.objects.filter(autor=request.user,fecha_fin__gte=date.today()).order_by("fecha_fin")[:6]
	#import pdb; pdb.set_trace()
	return render(request, 'casting/castingpanel.html',{'castings':castings, 'usercastings':usercastings,'fincastings':fincastings})