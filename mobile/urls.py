from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('mobile.views',
	url(r'^add-cliente/$', 'add_cliente', name = 'add_cliente'),
	url(r'^orden-servicio-lista/$', 'list_orden', name = 'list_orden'),
	url(r'^orden-servicio/$', 'orden_servicio_mobile', name = 'orden_servicio_mobile'),
	url(r'^find-vehiculo/$', 'find_vehiculo', name = 'find_vehiculo'),
	url(r'^new-vehiculo/$', 'new_vehiculo', name = 'new_vehiculo'),
	url(r'^delete-orden-servicio/(?P<orden>\d+)/$', 'delete_service', name = 'delete_service'),
	url(r'^add-service/(?P<orden>\d+)/$', 'add_service', name = 'add_service'),
	url(r'^delete-detalle/(?P<orden_detalle>\d+)/$', 'delete_detalle', name = 'delete_detalle'),
	url(r'^close-orden/(?P<orden>\d+)/$', 'close_orden_servicio', name = 'close_orden_servicio'),
	url(r'^new-orden-detalle/(?P<orden>\d+)/$', 'orden_servicio_detalle', name = 'orden_servicio_detalle'),
)