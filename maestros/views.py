# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, HttpResponse

import json
from datetime import datetime, time, timedelta
from maestros.models import mecanicoModel
from ordenes_servicios.models import ordenServicioDetalleModel
from maestros.forms import mecanicoModelForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from usuarios.models import *

class detailMecanicosView(DetailView):
	template_name = 'detail_mecanicos.html'
	model = mecanicoModel

	def get_context_data(self, **kwargs):
		context = super(detailMecanicosView, self).get_context_data(**kwargs)
		return context

class listMecanicosView(ListView):
	template_name = 'list_mecanicos.html'
	model = mecanicoModel
	context_object_name = 'mecanicos'
	paginate_by = 10

	@method_decorator(user_passes_test(lambda u: u.usuariosmodel.tipoUsuario.nombre_tipo == 'Administrador', login_url='/'))
	def dispatch(self, *args, **kwargs):
		return super(listMecanicosView,  self).dispatch(*args, **kwargs)

class createMecanicoView(SuccessMessageMixin, CreateView):
	template_name = 'create_mecanicos.html'
	form_class = mecanicoModelForm
	success_url = '/mecanicos'
	success_message = 'Se añadio con exito el Mecánico'

	@method_decorator(user_passes_test(lambda u: u.usuariosmodel.tipoUsuario.nombre_tipo == 'Administrador', login_url='/'))
	def dispatch(self, *args, **kwargs):
		return super(createMecanicoView,  self).dispatch(*args, **kwargs)

	def form_valid(self, form):
		tipo_usuario = tipoUsuario.objects.get(nombre_tipo = 'Mecanico')
		mecanico = form.save(commit = False)
		username = form.cleaned_data['email']
		password = mecanico.documento
		user = User.objects.create_user(username, form.cleaned_data['email'], password)
		user.first_name = mecanico.nombre
		user.last_name = mecanico.apellido
		user.save()
		perfil_mecanico = usuariosModel(usuario = user, tipoUsuario = tipo_usuario)
		perfil_mecanico.save()
		mecanico.cuenta = perfil_mecanico
		mecanico.save()
		return super(createMecanicoView, self).form_valid(form)

class updateMecanicoView(SuccessMessageMixin, UpdateView):
	model = mecanicoModel
	form_class = mecanicoModelForm
	template_name = 'create_mecanicos.html'
	success_url = '/mecanicos'
	success_message = 'Se ha actualizado con exito el mecanico'

	@method_decorator(user_passes_test(lambda u: u.usuariosmodel.tipoUsuario.nombre_tipo == 'Administrador', login_url='/'))
	def dispatch(self, *args, **kwargs):
		return super(updateMecanicoView, self).dispatch(*args, **kwargs)

	def form_valid(self, form):
		tipo_usuario = tipoUsuario.objects.get(nombre_tipo = 'Mecanico')
		mecanico = form.save(commit = False)
		try:
			cuenta_mecanico = User.objects.get(email = form.cleaned_data['email'])
			cuenta_mecanico.first_name = mecanico.nombre
			cuenta_mecanico.last_name = mecanico.apellido
			cuenta_mecanico.username = form.cleaned_data['email']
			cuenta_mecanico.email = form.cleaned_data['email']
			cuenta_mecanico.save()
			mecanico.save()
		except ObjectDoesNotExist:
			password = mecanico.documento
			user = User.objects.create_user(form.cleaned_data['email'], form.cleaned_data['email'], password)
			user.first_name = mecanico.nombre
			user.last_name = mecanico.apellido
			user.save()
			perfil_mecanico = usuariosModel(usuario = user, tipoUsuario = tipo_usuario)
			perfil_mecanico.save()
			mecanico.cuenta = perfil_mecanico
			mecanico.save()
		return super(updateMecanicoView, self).form_valid(form)

@login_required
@user_passes_test(lambda u: u.usuariosmodel.tipoUsuario.nombre_tipo == 'Administrador', login_url='/')
def time_mecanicos(request):
	mecanicos = mecanicoModel.objects.all()
	return render(request, 'time_mecanicos.html', {'mecanicos': mecanicos})

def disp_mecanico(request):
	response = {}
	mecanico_pk =  request.GET.get('mecanico_pk')
	mecanico = mecanicoModel.objects.get(pk = mecanico_pk)
	servicio_mecanico = ordenServicioDetalleModel.objects.filter(mecanico = mecanico)
	sum_tot = datetime.strptime('00:00:00', '%H:%M:%S')
	for hour in servicio_mecanico:
		time_service =  hour.servicio.time
		hour = time_service.hour
		minute = time_service.minute
		sum_tot = sum_tot + timedelta(hours = hour, minutes = minute)
	if sum_tot.hour <= 7:
		response['msg'] = 'Mecanico Disponible'
		response['type'] = True
	else:
		response['msg'] = 'Mecanico no Disponible'
		response['type'] = False
	return HttpResponse(json.dumps(response), content_type = 'application/json')