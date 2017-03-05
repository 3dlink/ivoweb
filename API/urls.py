from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^login/', LoginView.as_view()),
	url(r'^talentos/', TalentosView.as_view()),
	url(r'^relacion/', Usuario_ArteView.as_view()),
	
   ]   