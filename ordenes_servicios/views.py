# -*- encoding: utf-8 -*-
# import ho.pisa as pisa

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app.utils import get_or_none
from ordenes_servicios.forms import *
from vehiculos.models import vehiculoModel
from articulos_servicios.models import servicioModel
from ordenes_servicios.models import *
from maestros.models import mecanicoModel

from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.db.models import Sum
from easy_pdf.views import PDFTemplateView
from django.contrib.auth.decorators import login_required, user_passes_test
import json

@login_required
#@user_passes_test(lambda u: u.usuariosmodel.tipoUsuario.nombre_tipo == 'Administrador', login_url='/')
def detalleOrdenServicio(request, pk):
	sum_tot = 0
	orden = get_or_none(ordenServicioModel, pk=pk)
	ordenDetalle = ordenServicioDetalleModel.objects.filter(ordenServicio = orden)

	context = {
		'orden' : orden,
		'ordenDetalle' : ordenDetalle,
		'total_valor': ordenDetalle.aggregate(Sum('valorTotal'))
	}
	return render(request,'detail_orden_servicio.html', context)

@login_required
@user_passes_test(lambda u: u.usuariosmodel.tipoUsuario.nombre_tipo == 'Administrador', login_url='/')
@csrf_exempt
def guardarOrden(request):
	if request.method == "POST":
		placa = request.POST.get('placa')
		servicios = request.POST.getlist('servicios[]')
		cantidades = request.POST.getlist('cantidades[]')
		mecanicos = request.POST.getlist('mecanicos[]')

		if 'orden' in request.GET:
			orden = ordenServicioModel(pk=request.GET.get('orden'))
		else:
			vehiculo = get_or_none(vehiculoModel, placa=placa)
			orden = ordenServicioModel(vehiculo=vehiculo)
			orden.save()

		for i in range(0,len(servicios)):
			servicio = get_or_none(servicioModel, pk=servicios[i])
			cantidad = cantidades[i]
			mecanico = get_or_none(mecanicoModel, pk=mecanicos[i])
			total = int(servicio.valor)* int(cantidad)
			time = get_time(servicio.time)
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

@login_required
@user_passes_test(lambda u: u.usuariosmodel.tipoUsuario.nombre_tipo == 'Administrador', login_url='/')
def ordenServicioNueva(request, pk):

	vehiculo = get_or_none(vehiculoModel, placa=pk)
	form = ordenServicioDetalle()

	context = {
		'vehiculo' : vehiculo,
		'formDetalleOrden' : form
	}
	return render(request,'create_orden_servicio.html', context)

@login_required
@user_passes_test(lambda u: u.usuariosmodel.tipoUsuario.nombre_tipo == 'Administrador', login_url='/')
def ordenServicioEditar(request, pk, orden):

	vehiculo = get_or_none(vehiculoModel, placa=pk)
	orden = ordenServicioModel.objects.get(pk = orden)
	form = ordenServicioDetalle()

	context = {
		'vehiculo' : vehiculo,
		'formDetalleOrden' : form,
		'orden': orden
	}
	return render(request,'edit_orden_servicio.html', context)

@login_required
@user_passes_test(lambda u: u.usuariosmodel.tipoUsuario.nombre_tipo == 'Administrador', login_url='/')
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

@login_required
@user_passes_test(lambda u: u.usuariosmodel.tipoUsuario.nombre_tipo == 'Administrador', login_url='/')
def getServicioValor(request):
	if request.is_ajax():
		codigoServicio = request.GET.get('servicio')
		servicio = get_or_none(servicioModel, pk=codigoServicio)
		
		return JsonResponse(
			{'valor' : servicio.valor, 'detalle': servicio.detail },
			safe=False
		)

@login_required
@user_passes_test(lambda u: u.usuariosmodel.tipoUsuario.nombre_tipo == 'Administrador', login_url='/')
def orden_servicio_auto(request):
	form = ordenServicioAutoForm()
	if request.method == "POST":
		form = ordenServicioAutoForm(request.POST)
	return render(request, 'orden_servicio_auto.html', {'forms': form})

@login_required
@user_passes_test(lambda u: u.usuariosmodel.tipoUsuario.nombre_tipo == 'Administrador', login_url='/')
def orden_servicio_mecanico(request):
	form = ordenServicioMecanicoForm()
	if request.method == "POST":
		form = ordenServicioMecanicoForm(request.POST)
	return render(request, 'orden_servicio_mecanico.html', {'forms': form})

@login_required
@user_passes_test(lambda u: u.usuariosmodel.tipoUsuario.nombre_tipo == 'Administrador', login_url='/')
def ordenes_por_servicios(request):
	form = ordenPorServicioForm()
	if request.method == "POST":
		form = ordenPorServicioForm(request.POST)
	return render(request, 'ordenes_por_servicios.html', {'forms': form})

@login_required
@user_passes_test(lambda u: u.usuariosmodel.tipoUsuario.nombre_tipo == 'Administrador', login_url='/')
def delete_orden_servicio(request, pk):
	response = {}
	orden = ordenServicioDetalleModel.objects.get(pk = pk)
	orden.delete()
	return HttpResponse(json.dumps(response), "application/json")

class OrdenReporteAutoPDFView(PDFTemplateView):
	template_name = "pdf_orden_reporte_auto.html"

	def get_context_data(self, **kwargs):
		context = super(OrdenReporteAutoPDFView, self).get_context_data(**kwargs)
		fecha_in = self.kwargs['fecha_in']
		fecha_fin = self.kwargs['fecha_fin']
		placa = self.kwargs['placa']
		orden_servicio = ordenServicioModel.objects.filter(fecha__range = [fecha_in, fecha_fin])
		if placa != 'ALL':
			placa = vehiculoModel.objects.get(placa = self.kwargs['placa'])
			orden_servicio = ordenServicioModel.objects.filter(vehiculo = placa)
		orden_servicio.filter(fecha__range = [fecha_in, fecha_fin])
		context['orden_servicio'] = orden_servicio
		return context

class OrdenReporteMecanicoPDFView(PDFTemplateView):
	template_name = "pdf_orden_reporte_mecanico.html"

	def get_context_data(self, **kwargs):
		context = super(OrdenReporteMecanicoPDFView, self).get_context_data(**kwargs)
		mecanico = self.kwargs['mecanico']
		fecha_in = self.kwargs['fecha_in']
		fecha_fin = self.kwargs['fecha_fin']
		orden_servicio = ordenServicioDetalleModel.objects.all()
		if mecanico != 'ALL':
			orden_servicio.filter(mecanico = mecanico)
		context['orden_servicio'] = orden_servicio
		context['fecha_in'] = fecha_in
		context['fecha_fin'] = fecha_fin
		return context

class OrdenesPorServicioReportePDFView(PDFTemplateView):
	template_name = "pdf_ordenes_por_servicios_reporte.html"

	def get_context_data(self, **kwargs):
		context = super(OrdenesPorServicioReportePDFView, self).get_context_data(**kwargs)
		servicio = self.kwargs['servicio']
		fecha_in = self.kwargs['fecha_in']
		fecha_fin = self.kwargs['fecha_fin']
		servicio_data = ordenServicioDetalleModel.objects.filter(fecha__range = [fecha_in, fecha_fin])
		if servicio != 'ALL':
			servicio_data.filter(servicio = servicio)
		context['servicio_data'] = servicio_data
		return context

class OrdenServicioReportePDFView(PDFTemplateView):
	template_name = "pdf_orden_servicio_reporte.html"

	def get_context_data(self, **kwargs):
		context = super(OrdenServicioReportePDFView, self).get_context_data(**kwargs)
		orden_pk = self.kwargs['orden_pk']
		servicio_data = ordenServicioModel.objects.get(pk = orden_pk)
		ordenDetalle = ordenServicioDetalleModel.objects.filter(ordenServicio = servicio_data)
		context['servicio_data'] = servicio_data
		context['total_valor'] = ordenDetalle.aggregate(Sum('valorTotal'))
		return context