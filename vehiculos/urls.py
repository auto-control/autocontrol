from django.conf.urls import include, url

urlpatterns = [
	url(r'^historial/$', 'vehiculos.views.historialVehiculo', name = 'historial'),
]