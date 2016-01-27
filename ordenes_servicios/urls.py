from django.conf.urls import include, url

urlpatterns = [
	url(r'^orden-servicio/$', 'ordenes_servicios.views.ordenServicio', name = 'orden_servicio'),
	url(r'^orden-servicio/nueva/(?P<pk>[\w\-]+)/$', 'ordenes_servicios.views.ordenServicioNueva', name = 'create_orden_servicio'),
	url(r'^guardar-orden/$', 'ordenes_servicios.views.guardarOrden', name = 'guardar_orden'),
	url(r'^orden-servicio/(?P<pk>[\w\-]+)/$', 'ordenes_servicios.views.detalleOrdenServicio', name = 'detalle_orden_servicio'),
	url(r'^pdf/$', 'ordenes_servicios.views.pdf', name = 'pdf'),

	#Ajax request Urls
	url(r'^getServicioValor/$','ordenes_servicios.views.getServicioValor', name = 'get_servicio_valor'),
]