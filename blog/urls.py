from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^all/$', todos, name='todos'),    
    url(r'^post/(?P<idpost>[0-9]+)/$', detalle, name='detalle'),
    url(r'^busqueda/$', busqueda, name='busqueda'),
    url(r'^(?P<idcategoria>[A-Za-z]+)/$', posts_por_categoria, name='categoria'),

   
]