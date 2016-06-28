from django.conf.urls import include, url

from vehiculos.views import *

urlpatterns = [
	url(r'^historial/$', 'vehiculos.views.historialVehiculo', name = 'historial'),
	url(r'^historial/(?P<pk>[\w\-]+)/$', vehiculoDetail.as_view(), name = 'detail_vehiculo'),
	url(r'^vehiculo/nuevo/$', createVehiculoView.as_view(), name = 'create_vehiculo'),
	url(r'^vehiculo/actualizar/(?P<pk>[\w\-]+)/$', updateVehiculoView.as_view(), name = 'update_vehiculo'),
	url(r'^vehiculo/$', listVehiculosView.as_view(), name = 'list_vehiculo'),
	url(r'^obtener-linea/(?P<marca>[\w\-]+)/$', 'vehiculos.views.getLinea', name = 'get_linea'),

]