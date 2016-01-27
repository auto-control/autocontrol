# -*- encoding: utf-8 -*-

import ho.pisa as pisa

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt


from app.utils import get_or_none
from ordenes_servicios.forms import vehiculoOrdenForm, ordenServicioDetalle
from vehiculos.models import vehiculoModel
from articulos_servicios.models import servicioModel
from ordenes_servicios.models import ordenServicioModel, ordenServicioDetalleModel
from maestros.models import mecanicoModel


import ho.pisa as pisa
import cStringIO as StringIO
import cgi
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponse

def generar_pdf(html):
		# Función para generar el archivo PDF y devolverlo mediante HttpResponse
		result = StringIO.StringIO()
		pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
		if not pdf.err:
				return HttpResponse(result.getvalue(),mimetype='application/pdf')
		return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))

def pdf(request):
		# vista de ejemplo con un hipotético modelo Libro
		html = "<h1>Hola Mundo</h1>"
		return generar_pdf(html)

def detalleOrdenServicio(request, pk):
	orden = get_or_none(ordenServicioModel, pk=pk)
	ordenDetalle = ordenServicioDetalleModel.objects.filter(ordenServicio=orden)

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
			total = int(servicio.valor)* int(cantidad)
			print total

			ordenDetalle = ordenServicioDetalleModel(
				servicio = servicio,
				cantidad = cantidad,
				valorUnitario = servicio.valor,
				valorTotal = total,
				mecanico = mecanico,
				ordenServicio = orden
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