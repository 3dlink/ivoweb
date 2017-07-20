from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    url(r'^artistas/$', artistas, name='artistas'),
    url(r'^artistas/(?P<idcategoria>[0-9]+)/$', artista_por_categoria, name='artista_categoria'),
    url(r'^industrias/$', industrias, name='industrias'),
    url(r'^industrias/(?P<idcategoria>[0-9]+)/$', industria_por_categoria, name='industria_categoria'),
    url(r'^proveedores/$', proveedores, name='proveedores'),
    url(r'^proveedores/(?P<idcategoria>[0-9]+)/$', proveedor_por_categoria, name='proveedor_categoria'),
   
]