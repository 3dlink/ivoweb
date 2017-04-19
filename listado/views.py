from django.shortcuts import render_to_response, render
from frontend.models import  User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post
from frontend.models import UsuarioArteGenero, TipoArte, GeneroArtistico, UsuarioArte

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


# FALLA CON CUALQUIER REGISTRO NUEVO?

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














	# posts = Post.objects.all().order_by("-fecha_creacion")[:5]
	# all_users = User.objects.filter(tipo_usuario='A')
	# paginator = Paginator(all_users, 12) # Show 25 contacts per page

	# page = request.GET.get('page',1)
	# try:
	# 	result = paginator.page(page)
	# except PageNotAnInteger:
 #        # If page is not an integer, deliver first page.
	# 	result = paginator.page(1)
	# except EmptyPage:
 #        # If page is out of range (e.g. 9999), deliver last page of results.
	# 	result = paginator.page(paginator.num_pages)
	# import pdb;   pdb.set_trace()
	# return render_to_response("listado/artistas.html", {"artistas":result, "posts":posts }, )



	
	

