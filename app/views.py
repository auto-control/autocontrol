# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from ordenes_servicios.models import *
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
def home(request):
	if request.user.usuariosmodel.tipoUsuario.nombre_tipo == 'Mecanico':
		ordenesPendientesM = ordenServicioDetalleModel.objects.filter(mecanico = request.user.usuariosmodel.mecanicomodel_set.get().pk)
		context = {
			'ordenesPendientesM' : ordenesPendientesM
		}
	if request.user.usuariosmodel.tipoUsuario.nombre_tipo == 'Administrador':
		ordenesPendientes = ordenServicioModel.objects.order_by('-state', '-fecha')
		context = {
			'ordenesPendientes' : ordenesPendientes
		}
	if request.user.usuariosmodel.tipoUsuario.nombre_tipo == 'Cliente':
		cliente = request.user.usuariosmodel.clientemodel_set.get().vehiculomodel_set.all()
		ordenesPendientes = ordenServicioModel.objects.filter(vehiculo__in = cliente).order_by('-state', '-fecha')
		context = {
			'ordenesPendientes' : ordenesPendientes
		}
	return render(request, 'home.html', context)

@login_required
@user_passes_test(lambda u: u.usuariosmodel.tipoUsuario.nombre_tipo == 'Administrador', login_url='/')
def close_service(request, orden):
	orden = ordenServicioModel.objects.get(pk=orden)
	orden.state = 0
	orden.save(update_fields = ['state'])
	return HttpResponseRedirect('/')