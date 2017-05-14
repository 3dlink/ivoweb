from django.shortcuts import render_to_response, render
from frontend.models import  User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post
from frontend.models import UsuarioArteGenero, TipoArte, GeneroArtistico, UsuarioArte, SectorIndustria, Industria

# Create your views here.





def artistas(request):

	posts = Post.objects.all().order_by("-fecha_creacion")[:5]
	all_users = UsuarioArteGenero.objects.all()
	paginator = Paginator(all_users, 12) # Show 25 contacts per page
	tipoartes= TipoArte.objects.all()
	page = request.GET.get('page',1)
	try:
		result = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		result = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		result = paginator.page(paginator.num_pages)
	#import pdb;   pdb.set_trace()
	return render(request, "listado/artistas.html", {"artistas":result, "posts":posts, 'tipoartes':tipoartes } )



def artista_por_categoria(request, idcategoria):
	posts = Post.objects.all().order_by("-fecha_creacion")[:5]
	categoria = TipoArte.objects.get(name=idcategoria)
	generos = GeneroArtistico.objects.filter(id_tipo_arte=categoria).values('id')
	all_users = UsuarioArteGenero.objects.filter(id_genero__in=generos)
	tipoartes= TipoArte.objects.all()
	paginator = Paginator(all_users, 12) # Show 25 contacts per page	
	page = request.GET.get('page',1)
	try:
		result = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		result = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		result = paginator.page(paginator.num_pages)
	#import pdb;   pdb.set_trace()
	return render(request,"listado/artistas.html", {"artistas":result, "posts":posts,'tipoartes':tipoartes } )


def industrias(request):

	posts = Post.objects.all().order_by("-fecha_creacion")[:5]
	all_users = SectorIndustria.objects.filter(id_usuario__in=User.objects.filter(tipo_usuario='I').values_list('id',flat=True))
	paginator = Paginator(all_users, 12) # Show 25 contacts per page
	tipoindustrias= Industria.objects.filter(tipo='I')
	page = request.GET.get('page',1)
	try:
		result = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		result = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		result = paginator.page(paginator.num_pages)
	#import pdb;   pdb.set_trace()
	return render(request, "listado/industrias.html", {"industrias":result, "posts":posts, 'tipoindustrias':tipoindustrias } )


# FALLA CON CUALQUIER REGISTRO NUEVO?

def industria_por_categoria(request, idcategoria):
	posts = Post.objects.all().order_by("-fecha_creacion")[:5]
	#categoria = Industria.objects.get(nombre=idcategoria)
	all_users = SectorIndustria.objects.filter(id_sector=idcategoria)
	tipoindustrias= Industria.objects.all()
	paginator = Paginator(all_users, 12) # Show 25 contacts per page	
	page = request.GET.get('page',1)
	try:
		result = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		result = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		result = paginator.page(paginator.num_pages)
	#import pdb;   pdb.set_trace()
	return render(request,"listado/industrias.html", {"industrias":result, "posts":posts,'tipoindustrias':tipoindustrias } )


def proveedores(request):

	posts = Post.objects.all().order_by("-fecha_creacion")[:5]
	all_users = SectorIndustria.objects.filter(id_usuario__in=User.objects.filter(tipo_usuario='P').values_list('id',flat=True))
	paginator = Paginator(all_users, 12) # Show 25 contacts per page
	tipoindustrias= Industria.objects.filter(tipo='P')
	page = request.GET.get('page',1)
	try:
		result = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		result = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		result = paginator.page(paginator.num_pages)
	#import pdb;   pdb.set_trace()
	return render(request, "listado/proveedores.html", {"industrias":result, "posts":posts, 'tipoindustrias':tipoindustrias } )


# FALLA CON CUALQUIER REGISTRO NUEVO?

def proveedor_por_categoria(request, idcategoria):
	posts = Post.objects.all().order_by("-fecha_creacion")[:5]
	#categoria = Industria.objects.get(nombre=idcategoria)
	all_users = SectorIndustria.objects.filter(id_sector=idcategoria)
	tipoindustrias= Industria.objects.all()
	paginator = Paginator(all_users, 12) # Show 25 contacts per page	
	page = request.GET.get('page',1)
	try:
		result = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		result = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		result = paginator.page(paginator.num_pages)
	#import pdb;   pdb.set_trace()
	return render(request,"listado/proveedores.html", {"industrias":result, "posts":posts,'tipoindustrias':tipoindustrias } )