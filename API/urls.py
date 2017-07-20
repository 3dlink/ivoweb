from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from .views import *

urlpatterns = [
	url(r'^menu/(?P<email>[\w.%+-_]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', MenuUsuarioView.as_view()),
	url(r'^numseg/(?P<email>[\w.%+-_]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', NumeroSeguidoresView.as_view()),
	url(r'^artistas/$',TalentosView.as_view()),
	url(r'^artistas/(?P<idcategoria>[A-Za-z]+)/$', TalentosTipoView.as_view()),
	url(r'^proveedores/$',ProveedoresView.as_view()),
	url(r'^proveedores/(?P<idcategoria>[A-Za-z]+)/$',ProveedoresTipoView.as_view()),
	url(r'^castings/$',CastingsView.as_view()),
	url(r'^castings/(?P<idcategoria>[A-Za-z0-9]+)/$',CastingsTipoView.as_view()),
	url(r'^tipoarte/$', TipoArteView.as_view()),
	url(r'^tipoindustria/$', TipoIndustriaView.as_view()),
	url(r'^registro/', RegistroView.as_view()),
	url(r'^categoria/(?P<idcategoria>[A-Za-z]+)/$', UserCategoriaView.as_view()),
	url(r'^usuario/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/(?P<tab>[A-Za-z]+)/$', UsuarioView.as_view()),
	url(r'^login/', obtain_jwt_token),
    url(r'^verificar/', verify_jwt_token),
    url(r'^renovar/', refresh_jwt_token),
   ]   