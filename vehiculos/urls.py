from django.conf.urls import include, url

from vehiculos.views import vehiculoDetail

urlpatterns = [
	url(r'^historial/$', 'vehiculos.views.historialVehiculo', name = 'historial'),
	url(r'^historial/(?P<pk>[\w\-]+)/$', vehiculoDetail.as_view(), name = 'detail_vehiculo'),
]