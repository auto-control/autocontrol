from django.conf.urls import include, url
from django.contrib import admin

from auto_control import settings

urlpatterns = [
		url('', include('app.urls')),
		url('', include('clientes.urls')),
		url('', include('articulos_servicios.urls')),
		url('', include('maestros.urls')),
		url('', include('ordenes_servicios.urls')),
		url('', include('vehiculos.urls')),
		url('mobile/', include('mobile.urls')),
		url(r'^admin/', include(admin.site.urls)),

		url(r'^media/(?P<path>.*)$','django.views.static.serve',
				{'document_root': settings.MEDIA_ROOT,}
		),
]
