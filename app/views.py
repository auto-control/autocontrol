# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from ordenes_servicios.models import ordenServicioModel

def inicio(request):
	return render(request, 'base.html')


def home(request):
	ordenesPendientes = ordenServicioModel.objects.order_by('-state', '-fecha')
	context = {
		'ordenesPendientes' : ordenesPendientes
	}
	return render(request, 'home.html', context)

def close_service(request, orden):
	orden = ordenServicioModel.objects.get(pk=orden)
	orden.state = 0
	orden.save(update_fields = ['state'])
	return HttpResponseRedirect('/')