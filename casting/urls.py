from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    url(r'^inicio/$', todos, name='casting_inicio'),
    url(r'^categoria/(?P<idcategoria>[A-Za-z-\w]+)/$', casting_por_categoria, name='casting_categoria'),
    url(r'^id/(?P<idcasting>[0-9]+)/$', detalle, name='casting_detalle'),
    url(r'^crear/$', login_required(crear), name='casting_crear'),
    url(r'^guardar/$', guardar, name='casting_guardar'),
    url(r'^audicion/(?P<casting>[0-9]+)/$', audicion1, name='casting_audicion1'),
    url(r'^panel/$', login_required(panel), name='panel'),
    url(r'^industria/(?P<idcasting>[0-9]+)/$', casting_ind, name='casting_ind'),
    url(r'^audi/(?P<idaudicion>[0-9]+)/$', casting_aud, name='casting_aud'),
    url(r'^ganador/$', casting_ganador, name='casting_ganador'),

]