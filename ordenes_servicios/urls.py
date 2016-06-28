from django.conf.urls import include, url
from .views import *

urlpatterns = [
	url(r'^orden-servicio/$', 'ordenes_servicios.views.ordenServicio', name = 'orden_servicio'),
	url(r'^orden-servicio/nueva/(?P<pk>[\w\-]+)/$', 'ordenes_servicios.views.ordenServicioNueva', name = 'create_orden_servicio'),
	url(r'^orden-servicio/editar/(?P<pk>[\w\-]+)/(?P<orden>[\w\-]+)/$', 'ordenes_servicios.views.ordenServicioEditar', name = 'edit_orden_servicio'),
	url(r'^orden-servicio/imprimir/(?P<pk>[\w\-]+)/$', 'ordenes_servicios.views.ordenServicioImprimir', name = 'imprimir_orden_servicio'),
	url(r'^guardar-orden/$', 'ordenes_servicios.views.guardarOrden', name = 'guardar_orden'),
	url(r'^orden-servicio/(?P<pk>[\w\-]+)/$', 'ordenes_servicios.views.detalleOrdenServicio', name = 'detalle_orden_servicio'),

	#Reportes
	url(r'^orden-servicio-auto/$', 'ordenes_servicios.views.orden_servicio_auto', name = 'orden_servicio_auto'),
	url(r'^orden-servicio-mecanico/$', 'ordenes_servicios.views.orden_servicio_mecanico', name = 'orden_servicio_mecanico'),
	url(r'^orden-servicio-reporte-auto/(?P<placa>[\w\-]+)/(?P<fecha_in>[\w\-]+)/(?P<fecha_fin>[\w\-]+)/$', OrdenReporteAutoPDFView.as_view(), name = 'orden_servicio_reporte_auto'),
	url(r'^orden-servicio-reporte-mecanico/(?P<mecanico>[\w\-]+)/(?P<fecha_in>[\w\-]+)/(?P<fecha_fin>[\w\-]+)/$', OrdenReporteMecanicoPDFView.as_view(), name = 'orden_servicio_reporte_mecanico'),

	#Ajax request Urls
	url(r'^getServicioValor/$','ordenes_servicios.views.getServicioValor', name = 'get_servicio_valor'),
	url(r'^mecanicos/tiempos$', 'maestros.views.time_mecanicos', name = 'time_mecanicos'),
	url(r'^mecanicos/disponibilidad/$', 'maestros.views.disp_mecanico', name = 'disp_mecanico'),

]