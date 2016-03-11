# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import CreateView, ListView

from articulos_servicios.forms import servicioModelForm
from articulos_servicios.models import servicioModel


class createServicioView(CreateView):
	template_name = 'create_servicio.html'
	form_class = servicioModelForm
	success_url = '/servicios/nuevo'


class listServicioView(ListView):
	template_name = 'list_servicio.html'
	model = servicioModel
	context_object_name = 'servicios'
	paginate_by = 10