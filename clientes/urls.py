from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from clientes.views import *

urlpatterns = [
	url(r'^clientes/$', listClientesView.as_view(), name = 'list_clientes'),
	url(r'^clientes/(?P<pk>\d+)/$', login_required(detailClientesView.as_view()), name = 'detail_clientes'),
	url(r'^clientes/nuevo$', createClienteView.as_view(), name = 'create_clientes'),
	url(r'^clientes/actualizar/(?P<pk>\d+)/$', updateClienteView.as_view(), name = 'update_clientes')
]