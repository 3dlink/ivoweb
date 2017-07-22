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
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
import notifications.urls




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^facebook-login/$', views.facebook_login, name='facebook'),
    url(r'^facebook-registro/$', views.facebook_registro, name='facebook-registro'),
    url(r'^registrate/$', views.registrate, name='registro'),
    url(r'^registrate/artista/$', views.registrate_artistas, name='registro_artistas'),
    url(r'^registrate/talentos/$', views.getArtes, name='registrate'),
    url(r'^registrate/generos-artisticos/$', views.getGeneroArtisticos, name='generos_artisticos'),
    url(r'^industria/$', views.industria, name='industria'),
    url(r'^ciudad/$', views.buscar_ciudad, name='ciudad'),
    url(r'^registro/industria/$', views.RegistroIndustria, name='industria'),
    url(r'^registro/proveedor/$', views.RegistroProveedor, name='proveedor'),
    url(r'^fan/$', views.fan, name='fan'),
    url(r'^registro/fan/$', views.registrofan, name='registrofan'),
    url(r'^registro/fan/interes$', views.faninteres, name='faninteres'),
    url(r'^castings/$', views.castings, name='castings'),
    url(r'^artistadashboard/$', login_required(views.artistadashboard), name='artistadashboard'),
    url(r'^busqueda-avanzada/$', login_required(views.busqueda_avanzada), name='busqueda_avanzada'),
    url(r'^industriadashboard/$', views.industriadashboard, name='industriadashboard'),
    url(r'^crearcasting/$', views.crearcasting, name='crearcasting'),
    url(r'^seleccion-registro/$', views.registrosecundario, name='seleccionregistro'),
    url(r'^seguir/$', views.seguir, name='seguir'),
    url(r'^terminos/$', views.terminos, name='terminos'),
    url(r'^planes/$', views.planes, name='planes'),
    url(r'^pagar/$', views.pagar, name='pagar'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^faq-busqueda/$', views.busqueda_pregunta, name='busqueda_pregunta'),
    url(r'^faq-pregunta/$', views.faqpregunta, name='faqpregunta'),
    url(r'^corporativa/$', views.corporativa, name='corporativa'),
    url(r'^corporativa/contacto/$', views.contacto, name='contacto'),
    url(r'^olvido-clave/$', views.olvidoclave, name='olvidoclave'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

    url(r'^mensaje/get_user/', views.get_user, name='get_user'),
    url(r'^busqueda/$', views.busqueda, name='busqueda'),
    
    #url(r'^artistas/$', views.artistas, name='listado'),

    #url(r'^accounts/',include('allauth.urls')),
    url(r'^login/', views.index, name='index'),
    url(r'^logout/', views.cerrar_sesion, name='logout'),
    url(r'^perfil/', include('perfiles.urls', namespace='perfiles')),
    url(r'^all/', include('listado.urls', namespace='listado')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^casting/', include('casting.urls', namespace='casting')),
    url(r'^api/v1/', include('API.urls', namespace='api')),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications'))
    

    
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
