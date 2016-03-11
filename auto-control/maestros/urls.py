from django.conf.urls import include, url

from .views import *

urlpatterns = [
	url(r'^mecanicos/$', listMecanicosView.as_view(), name = 'list_mecanicos'),
	url(r'^mecanicos/nuevo$', createMecanicoView.as_view(), name = 'create_mecanicos'),
]