from django.conf.urls import include, url
from usuarios.views import *


urlpatterns = [
	url(r'^ingresar/$', loginView.as_view(), name='ingresar')
]