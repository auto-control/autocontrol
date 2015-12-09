from django.conf.urls import include, url

from maestros.views import listMecanicosView, createMecanicoView

urlpatterns = [
	url(r'^mecanicos/$', listMecanicosView.as_view(), name = 'list_mecanicos'),
	url(r'^mecanicos/nuevo$', createMecanicoView.as_view(), name = 'create_mecanicos'),
]