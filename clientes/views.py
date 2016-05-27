# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from clientes.models import clienteModel
from clientes.forms import clienteModelForm


class listClientesView(ListView):
	queryset = clienteModel.objects.all().order_by('apellido')
	template_name = 'list_clientes.html'
	context_object_name = 'clientes'
	paginate_by = 10

class createClienteView(SuccessMessageMixin, CreateView):
	template_name = 'create_clientes.html'
	form_class = clienteModelForm
	success_url = '/clientes'
	success_message ='Se añadio con éxito el cliente!'

class updateClienteView(SuccessMessageMixin, UpdateView):
	model = clienteModel
	form_class = clienteModelForm
	template_name = 'create_clientes.html'
	success_url = '/clientes'
	success_message = 'Se ha actualizado con exito el cliente'