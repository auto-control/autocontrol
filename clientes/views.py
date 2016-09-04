# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from clientes.models import clienteModel
from clientes.forms import clienteModelForm
from django.core.exceptions import ObjectDoesNotExist
from usuarios.models import *

class detailClientesView(DetailView):
	template_name = 'detail_clientes.html'
	model = clienteModel

	def get_context_data(self, **kwargs):
		context = super(detailClientesView, self).get_context_data(**kwargs)
		return context

class listClientesView(ListView):
	queryset = clienteModel.objects.all().order_by('apellido')
	template_name = 'list_clientes.html'
	context_object_name = 'clientes'

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
		if cliente.email != "":
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

	def form_valid(self, form):
		tipo_usuario = tipoUsuario.objects.get(nombre_tipo = 'Cliente')
		cliente = form.save(commit = False)
		try:
			cuenta_cliente = User.objects.get(email = cliente.email)
			cuenta_cliente.first_name = cliente.nombre
			cuenta_cliente.last_name = cliente.apellido
			cuenta_cliente.username = cliente.email
			cuenta_cliente.email = cliente.email
			cuenta_cliente.set_password(cliente.documento)
			cuenta_cliente.save()
			cliente.save()
		except ObjectDoesNotExist:
			password = cliente.documento
			user = User.objects.create_user(cliente.email, cliente.email, password)
			user.first_name = cliente.nombre
			user.last_name = cliente.apellido
			user.save()
			perfil_cliente = usuariosModel(usuario = user, tipoUsuario = tipo_usuario)
			perfil_cliente.save()
			cliente.cuenta = perfil_cliente
			cliente.save()
		return super(updateClienteView, self).form_valid(form)