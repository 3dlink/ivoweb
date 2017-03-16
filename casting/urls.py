from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    url(r'^inicio/$', todos, name='casting_inicio'),
    url(r'^categoria/(?P<idcategoria>[A-Za-z-\w]+)/$', casting_por_categoria, name='casting_categoria'),
    url(r'^id/(?P<idcasting>[0-9]+)/$', detalle, name='casting_detalle'),
    url(r'^crear/$', crear, name='casting_crear'),
    url(r'^guardar/$', guardar, name='casting_guardar')

   
]