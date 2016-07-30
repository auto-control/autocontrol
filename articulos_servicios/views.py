# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from articulos_servicios.forms import servicioModelForm
from articulos_servicios.models import servicioModel
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

class createServicioView(CreateView):
	template_name = 'create_servicio.html'
	form_class = servicioModelForm
	success_url = '/servicios/nuevo'

	@method_decorator(user_passes_test(lambda u: u.usuariosmodel.tipoUsuario.nombre_tipo == 'Administrador', login_url='/'))
	def dispatch(self, *args, **kwargs):
		return super(createServicioView,  self).dispatch(*args, **kwargs)

class listServicioView(ListView):
	template_name = 'list_servicio.html'
	model = servicioModel
	context_object_name = 'servicios'
	paginate_by = 10

	@method_decorator(user_passes_test(lambda u: u.usuariosmodel.tipoUsuario.nombre_tipo == 'Administrador', login_url='/'))
	def dispatch(self, *args, **kwargs):
		return super(listServicioView,  self).dispatch(*args, **kwargs)