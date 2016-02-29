# -*- encoding: utf-8 -*-

# import ho.pisa as pisa

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app.utils import get_or_none
from ordenes_servicios.forms import vehiculoOrdenForm, ordenServicioDetalle
from vehiculos.models import vehiculoModel
from articulos_servicios.models import servicioModel
from ordenes_servicios.models import ordenServicioModel, ordenServicioDetalleModel
from maestros.models import mecanicoModel

from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.db.models import Sum
from datetime import datetime, time, timedelta


def ordenServicioImprimir(request, pk):
		orden = get_object_or_404(ordenServicioModel, pk=pk)
		ordenDetalle = ordenServicioDetalleModel.objects.filter(ordenServicio=orden)

		contexto = {
			'orden' : orden,
			'ordenDetalle' : ordenDetalle
		}

		html = render_to_string('imprimir_orden_servicio.html', contexto)
		return generar_pdf(html)

def detalleOrdenServicio(request, pk):
	sum_tot = 0
	orden = get_or_none(ordenServicioModel, pk=pk)
	ordenDetalle = ordenServicioDetalleModel.objects.filter(ordenServicio = orden)

	context = {
		'orden' : orden,
		'ordenDetalle' : ordenDetalle, 
	}
	return render(request,'detail_orden_servicio.html', context)

@csrf_exempt
def guardarOrden(request):
	if request.method == "POST":
		placa = request.POST.get('placa')
		servicios = request.POST.getlist('servicios[]')
		cantidades = request.POST.getlist('cantidades[]')
		mecanicos = request.POST.getlist('mecanicos[]')

		vehiculo = get_or_none(vehiculoModel, placa=placa)

		orden = ordenServicioModel(vehiculo=vehiculo)
		orden.save()

		for i in range(0,len(servicios)):
			servicio = get_or_none(servicioModel, pk=servicios[i])
			cantidad = cantidades[i]
			mecanico = get_or_none(mecanicoModel, pk=mecanicos[i])
			time_service = datetime.strptime(str(servicio.time), '%H:%M:%S')
			time_now = datetime.now()
			time = time_now + timedelta(hours = time_service.hour, minutes = time_service.minute)
			print time
			total = int(servicio.valor)* int(cantidad)
			ordenDetalle = ordenServicioDetalleModel(
				servicio = servicio,
				cantidad = cantidad,
				valorUnitario = servicio.valor,
				valorTotal = total,
				mecanico = mecanico,
				ordenServicio = orden,
				time = time
			)

			ordenDetalle.save()

		url = u'%s/%s' % ('/orden-servicio', orden.pk)
		return HttpResponseRedirect(url)

def ordenServicioNueva(request, pk):

	vehiculo = get_or_none(vehiculoModel, placa=pk)
	form = ordenServicioDetalle()

	context = {
		'vehiculo' : vehiculo,
		'formDetalleOrden' : form
	}
	return render(request,'create_orden_servicio.html', context)




def ordenServicio(request):

	form = vehiculoOrdenForm()
	message = ''
	if request.method == "POST":
		form = vehiculoOrdenForm(request.POST)
		if form.is_valid():
			placa = form.cleaned_data['placa']
			vehiculo = get_or_none(vehiculoModel, placa=placa)
			if vehiculo is not None:
				url = u'%s/%s' % ('/orden-servicio/nueva', placa)
				return HttpResponseRedirect(url)
			else:
				message = "El vehiculo no se encuentra registrado debe registrarlo."

	context = {
		'formVehiculo': form,
		'message' : message
	}

	return render(request, 'orden_servicio.html', context)


def getServicioValor(request):
	if request.is_ajax():
		codigoServicio = request.GET.get('servicio')
		servicio = get_or_none(servicioModel, pk=codigoServicio)
		
		return JsonResponse(
			{'valor' : servicio.valor },
			safe=False
		)