from django.conf.urls import include, url

from vehiculos.views import *

urlpatterns = [
	url(r'^SOAT/$', 'vehiculos.views.soat', name = 'soat'),
	url(r'^historial/$', 'vehiculos.views.historialVehiculo', name = 'historial'),
	url(r'^historial-vehiculo/(?P<pk>[\w\-]+)/$', vehiculoDetail.as_view(), name = 'detail_vehiculo'),
	url(r'^vehiculo/nuevo/$', createVehiculoView.as_view(), name = 'create_vehiculo'),
	url(r'^vehiculo/actualizar/(?P<pk>[\w\-]+)/$', updateVehiculoView.as_view(), name = 'update_vehiculo'),
	url(r'^vehiculo/$', listVehiculosView.as_view(), name = 'list_vehiculo'),
	url(r'^obtener-linea/(?P<marca>[\w\-]+)/$', 'vehiculos.views.getLinea', name = 'get_linea'),

	#Reportes
	url(r'^vehiculo-soat/$', 'vehiculos.views.vehiculo_soat', name = 'vehiculo_soat'),
	url(r'^vehivulo-reporte-soat/(?P<fecha_in>[\w\-]+)/(?P<fecha_fin>[\w\-]+)/$', ReporteSoatPDFView.as_view(), name = 'vehiculo_reporte_soat'),
]