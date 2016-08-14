from django.conf.urls import include, url
from articulos_servicios.views import *

urlpatterns = [
	url(r'^servicios/nuevo$', createServicioView.as_view(), name = 'create_servicio'),
	url(r'^servicios/$', listServicioView.as_view(), name = 'list_servicio'),
	url(r'^servicios/actualizar/(?P<pk>\d+)/$', updateServicioView.as_view(), name = 'update_servicios')
]