from django.conf.urls import include, url

from clientes.views import listClientesView, createClienteView

urlpatterns = [
	url(r'^clientes/$', listClientesView.as_view(), name = 'list_clientes'),
	url(r'^clientes/nuevo$', createClienteView.as_view(), name = 'create_clientes')
]