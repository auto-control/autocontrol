from django.conf.urls import include, url

from articulos_servicios.views import createServicioView, listServicioView

urlpatterns = [
	url(r'^servicios/nuevo$', createServicioView.as_view(), name = 'create_servicio'),
	url(r'^servicios/$', listServicioView.as_view(), name = 'list_servicio'),
]