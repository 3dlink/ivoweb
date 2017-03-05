"""ivotalents URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from frontend import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^registrate/$', views.registrate, name='registro'),
    url(r'^registrate/talentos/$', views.getArtes, name='registrate'),
    url(r'^registrate/generos-artisticos/$', views.getGeneroArtisticos, name='generos_artisticos'),
    url(r'^industria/$', views.industria, name='industria'),
    url(r'^proveedor/$', views.proveedor, name='proveedor'),
    url(r'^registro/industria/$', views.RegistroIndustria, name='industria'),
    url(r'^fan/$', views.fan, name='fan'),
    url(r'^registro/fan/$', views.registrofan, name='registrofan'),
    url(r'^registro/fan/interes$', views.faninteres, name='faninteres'),
    url(r'^castings/$', views.castings, name='castings'),
    url(r'^artistadashboard/$', views.artistadashboard, name='artistadashboard'),
    url(r'^industriadashboard/$', views.industriadashboard, name='industriadashboard'),
    url(r'^crearcasting/$', views.crearcasting, name='crearcasting'),
    url(r'^registroalternativo/$', views.registrosecundario, name='registroalternativo'),
    
    #url(r'^artistas/$', views.artistas, name='listado'),


    url(r'^login/', views.index, name='index'),
    url(r'^logout/', views.cerrar_sesion, name='logout'),

    url(r'^perfil/', include('perfiles.urls', namespace='perfiles')),
    url(r'^all/', include('listado.urls', namespace='listado')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    #url(r'^generos/', views.GeneroView.as_view()),
    url(r'^api/v1/', include('API.urls', namespace='api')),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
