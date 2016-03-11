from django.conf.urls import include, url

from vehiculos.views import vehiculoDetail, createVehiculoView, listVehiculosView

urlpatterns = [
	url(r'^historial/$', 'vehiculos.views.historialVehiculo', name = 'historial'),
	url(r'^historial/(?P<pk>[\w\-]+)/$', vehiculoDetail.as_view(), name = 'detail_vehiculo'),
	url(r'^vehiculo/nuevo$', createVehiculoView.as_view(), name = 'create_vehiculo'),
	url(r'^vehiculo/$', listVehiculosView.as_view(), name = 'list_vehiculo'),

]