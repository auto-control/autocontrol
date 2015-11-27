from django.conf.urls import include, url

from maestros.views import listMecanicosView

urlpatterns = [
	url(r'^mecanicos/$', listMecanicosView.as_view(), name = 'list_mecanicos'),
]