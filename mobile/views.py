import json
from app.utils import get_or_none
from django.shortcuts import render
from vehiculos.models import vehiculoModel
from clientes.forms import clienteModelForm
from django.core.urlresolvers import reverse
from vehiculos.forms import vehiculoModelForm
from django.views.decorators.csrf import csrf_exempt
from ordenes_servicios.forms import ordenServicioDetalle
from django.http import HttpResponse, HttpResponseRedirect
from ordenes_servicios.models import ordenServicioModel, ordenServicioDetalleModel

def orden_servicio_mobile(request):
	return render(request, 'orden-servicio-m.html', {'title': 'Orden de servicio'})

def new_vehiculo(request):
	response = {}
	if request.method == 'POST':
		form = vehiculoModelForm(request.POST, request.FILES)
		print form.errors
		if form.is_valid():
			form.save()
			response['msg'] = "Vehiculo creado"
		else:
			response['msg'] = "Ha ocurrido un error"
		return HttpResponse(json.dumps(response), content_type = 'application/json')
	else:
		form = vehiculoModelForm()
	return render(request, 'new-vehiculo.html', {'title': 'Nuevo vehiculo', 'forms': form})

@csrf_exempt
def find_vehiculo(request):
	response = {}
	if request.is_ajax:
		find = get_or_none(vehiculoModel, placa = request.POST.get('placa',''))
		response['response'] = find.placa if find is not None else None
		response['orden_servicio'] = new_orden_servicio(find) if find is not None else None
	else:
		response['response'] = 'Ha ocurrido un error'
	return HttpResponse(json.dumps(response), "application/json")

def orden_servicio_detalle(request, orden):
	try:
		orden = ordenServicioModel.objects.get(pk = orden)
		return render(request, 'orden-servicio-detalle-m.html', {'title': 'Detalle orden de servicio', 'orden': orden})
	except:
		return HttpResponseRedirect(reverse('orden_servicio_mobile'))

def add_service(request, orden):
	response = {}
	orden = get_or_none(ordenServicioModel, pk = orden)
	if request.method == 'POST':
		form = ordenServicioDetalle(request.POST, instance = orden)
		if form.is_valid():
			detalle_orden = form.save()
			response['pk'] = detalle_orden.pk
			response['detail'] = detalle_orden.servicio.detail
			response['servicio'] = detalle_orden.servicio.nombre
			response['mecanico'] = detalle_orden.mecanico.nombre
			response['valor'] = str("{0:,}".format(detalle_orden.servicio.valor))
		else:
			print form.errors
			response['response'] = "Ha ocurrido un error"
		return HttpResponse(json.dumps(response), content_type = 'application/json')
	else:
		form = ordenServicioDetalle(instance = orden, service = orden)
	return render(request, 'form-detalle-servicio.html', {'title': 'Detalle Orden de servicio No.'+str(orden.pk), 'forms': form, 'orden': orden.pk})

def delete_detalle(request, orden_detalle):
	response = {}
	orden = get_or_none(ordenServicioDetalleModel, pk = orden_detalle)
	orden.delete()
	response['msg'] = 'Eliminado'
	return HttpResponse(json.dumps(response), "application/json")

def delete_service(request, orden):
	response = {}
	orden = get_or_none(ordenServicioModel, pk = orden)
	orden.delete()
	response['msg'] = 'Eliminado'
	return HttpResponse(json.dumps(response), "application/json")

def close_orden_servicio(request, orden):
	orden = ordenServicioModel.objects.get(pk = orden)
	orden.state = 0
	orden.save(update_fields = ['state'])
	return HttpResponseRedirect(reverse('orden_servicio_mobile'))

def new_orden_servicio(vehiculo):
	orden_servicio = ordenServicioModel(vehiculo = vehiculo)
	orden_servicio.save()
	return orden_servicio.pk

def add_cliente(request):
	response = {}
	if request.method == 'POST':
		form = clienteModelForm(request.POST)
		if form.is_valid():
			form.save()
			response['msg'] = "Cliente agregado"
		else:
			response['msg'] = "Ha ocurrido un error"
		return HttpResponse(json.dumps(response), content_type = 'application/json')
	else:
		form = clienteModelForm()
	return render(request, 'form-new-cliente.html', {'title': 'Nuevo cliente', 'forms': form})

def list_orden(request):
	orden = ordenServicioModel.objects.all().order_by('-state', '-fecha')
	return render(request, 'orden-lista.html', {'title': 'Listado de Ordenes', 'ordenes': orden})