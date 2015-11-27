from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url('', include('app.urls')),
    url('', include('clientes.urls')),
    url('', include('articulos_servicios.urls')),
    url('', include('maestros.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
