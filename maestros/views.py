# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, HttpResponse

import json
from datetime import datetime, time, timedelta
from maestros.models import mecanicoModel
from ordenes_servicios.models import ordenServicioDetalleModel
from maestros.forms import mecanicoModelForm

class listMecanicosView(ListView):
	template_name = 'list_mecanicos.html'
	model = mecanicoModel
	context_object_name = 'mecanicos'
	paginate_by = 10

class createMecanicoView(SuccessMessageMixin, CreateView):
	template_name = 'create_mecanicos.html'
	form_class = mecanicoModelForm
	success_url = '/mecanicos'
	success_message = 'Se añadio con exito el Mecánico'

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