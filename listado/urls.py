from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    url(r'^artistas/$', artistas, name='artistas'),
    url(r'^artistas/(?P<idcategoria>[A-Za-z]+)/$', artista_por_categoria, name='artista_categoria'),
   
]