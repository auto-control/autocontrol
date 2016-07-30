# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from clientes.models import clienteModel
from clientes.forms import clienteModelForm
from usuarios.models import *

class listClientesView(ListView):
	queryset = clienteModel.objects.all().order_by('apellido')
	template_name = 'list_clientes.html'
	context_object_name = 'clientes'
	paginate_by = 10

	@method_decorator(user_passes_test(lambda u: u.usuariosmodel.tipoUsuario.nombre_tipo == 'Administrador', login_url='/'))
	def dispatch(self, *args, **kwargs):
		return super(listClientesView,  self).dispatch(*args, **kwargs)

class createClienteView(SuccessMessageMixin, CreateView):
	template_name = 'create_clientes.html'
	form_class = clienteModelForm
	success_url = '/clientes'
	success_message ='Se añadio con éxito el cliente!'

	@method_decorator(user_passes_test(lambda u: u.usuariosmodel.tipoUsuario.nombre_tipo == 'Administrador', login_url='/'))
	def dispatch(self, *args, **kwargs):
		return super(createClienteView,  self).dispatch(*args, **kwargs)

	def form_valid(self, form):
		tipo_usuario = tipoUsuario.objects.get(nombre_tipo = 'Cliente')
		cliente = form.save(commit = False)
		password = cliente.documento
		user = User.objects.create_user(cliente.email, cliente.email, password)
		user.first_name = cliente.nombre
		user.last_name = cliente.apellido
		user.save()
		perfil_cliente = usuariosModel(usuario = user, tipoUsuario = tipo_usuario)
		perfil_cliente.save()
		cliente.cuenta = perfil_cliente
		cliente.save()
		return super(createClienteView, self).form_valid(form)

class updateClienteView(SuccessMessageMixin, UpdateView):
	model = clienteModel
	form_class = clienteModelForm
	template_name = 'create_clientes.html'
	success_url = '/clientes'
	success_message = 'Se ha actualizado con exito el cliente'

	@method_decorator(user_passes_test(lambda u: u.usuariosmodel.tipoUsuario.nombre_tipo == 'Administrador', login_url='/'))
	def dispatch(self, *args, **kwargs):
		return super(updateClienteView,  self).dispatch(*args, **kwargs)