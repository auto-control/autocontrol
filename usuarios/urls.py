from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from usuarios.views import *

login_forbidden = user_passes_test(lambda u: u.is_anonymous(), '/')

urlpatterns = [
	#url(r'^ingresar/$', loginView.as_view(), name='ingresar')
	url(r'^ingresar/$', login_forbidden(auth_views.login), {'template_name': 'login.html'}, name = 'ingresar'),
	url(r'^salir/$', auth_views.logout, {'next_page': '/ingresar/'}, name = 'salir')
]