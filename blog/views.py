from django.shortcuts import render_to_response, render, redirect
from django.views.generic import TemplateView
from .models import Categoria, Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from  blog.forms import FormBusqueda
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from functools import reduce
from django.db.models import Q
# Create your views here.






def todos(request):
	#import pdb;   pdb.set_trace()
	all_posts = Post.objects.all().order_by("-fecha_creacion")
	paginator = Paginator(all_posts, 5) # Show 25 contacts per page

	page = request.GET.get('page',1)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		posts = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		posts = paginator.page(paginator.num_pages)
		#import pdb;   pdb.set_trace()
	return render(request, "blog/blog.html", {"posts": posts })


#def todos(request):
#	posts = Post.objects.order_by("-fecha_creacion")
	


def posts_por_categoria(request, idcategoria):
	categoria = Categoria.objects.get(nombre=idcategoria)
	all_posts = categoria.post_set.order_by("-fecha_creacion")
	paginator = Paginator(all_posts, 5) # Show 25 contacts per page	
	page = request.GET.get('page',1)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		posts = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		posts = paginator.page(paginator.num_pages)
		#import pdb;   pdb.set_trace()
		
	return render(request, "blog/blog.html", {"posts": posts })



def detalle(request,idpost):

	post = Post.objects.get(id=idpost)
	#import pdb;   pdb.set_trace()
	return render(request,"blog/post.html", {"post": post, },)


def busqueda(request):

	
	terms = request.GET['q']
	term_list = terms.split(' ')

	results = Post.objects.all()

	qq = Q(titulo__icontains=term_list[0]) | Q(contenido__icontains=term_list[0])
	for term in term_list[1:]:
		qq.add((Q(contenido__icontains=term) | Q(titulo__icontains=term)), qq.connector)

	results = results.filter(qq)
	
	#import pdb;pdb.set_trace()
	paginator = Paginator(results, 6)
	page = request.GET.get('page',1)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:	       
		posts = paginator.page(1)
	except EmptyPage:	       
		posts = paginator.page(paginator.num_pages)			
	return render(request,"blog/resultados.html", {"posts": posts})
	
