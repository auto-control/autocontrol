from django.conf.urls import include, url


urlpatterns = [
	url(r'^orden-servicio/$', 'ordenes_servicios.views.ordenServicio', name = 'create_orden_servicio'),
]