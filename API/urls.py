from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from .views import *

urlpatterns = [
	url(r'^generos/', GenerosView.as_view()),
	url(r'^registro/', RegistroView.as_view()),
	url(r'^categoria/(?P<idcategoria>[A-Za-z]+)/$', UserCategoriaView.as_view()),	
	url(r'^login/', obtain_jwt_token),
    url(r'^verificar/', verify_jwt_token),
    url(r'^renovar/', refresh_jwt_token),
   ]   