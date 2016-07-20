# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView, CreateView, ListView, UpdateView


from app.utils import get_or_none
from django.core import serializers
from django.views.generic import DetailView
from easy_pdf.views import PDFTemplateView
from ordenes_servicios.models import ordenServicioModel
from vehiculos.models import *
from vehiculos.forms import *
import datetime

def historialVehiculo(request):
	form = buscarVehiculoHistorialForm()
	message = ''
	if request.method == 'POST':
		form = buscarVehiculoHistorialForm(request.POST)
		if form.is_valid():
			placa = form.cleaned_data['placa']
			vehiculo = get_or_none(vehiculoModel, placa=placa)
			if vehiculo is not None:
				url = '/historial-vehiculo/'+str(vehiculo.pk)+'/'
				return HttpResponseRedirect(url)
			else:
				message = "El vehiculo no se encuentra registrado."

	context = {
		'form' : form,
		'message' : message,
	}
	return render(request, 'historial_vehiculo.html', context)


class vehiculoDetail(DetailView):
	template_name = 'detail_vehiculo.html'
	model = vehiculoModel
	context_object_name = 'vehiculo'

	def get_context_data(self, **kwargs):
		context = super(vehiculoDetail, self).get_context_data(**kwargs)
		context["ordenes_servicios"] = self.get_ordenes_servicios()
		return context

	def get_ordenes_servicios(self):
		vehiculo = self.object
		ordenesServicios = ordenServicioModel.objects.filter(vehiculo=vehiculo)
		return ordenesServicios

def getLinea(request, marca):
	current_marca = MarcaModel.objects.get(pk=marca)
	models = tipoLineaModel.objects.filter(marca=current_marca)
	json_models = serializers.serialize("json", models)
	return HttpResponse(json_models, content_type = 'application/json')

class createVehiculoView(SuccessMessageMixin, CreateView):
	template_name = 'create_vehiculo.html'
	form_class = vehiculoModelForm
	success_url = '/vehiculo'
	success_message ='Se añadio con éxito el vehiculo!'

class updateVehiculoView(SuccessMessageMixin, UpdateView):
	model = vehiculoModel
	form_class = vehiculoModelForm
	template_name = 'create_vehiculo.html'
	success_url = '/vehiculo'
	success_message = 'Se ha actualizado con exito el vehiculo'

class listVehiculosView(ListView):
	template_name = 'list_vehiculo.html'
	model = vehiculoModel
	context_object_name = 'vehiculos'
	paginate_by = 10

def vehiculo_soat(request):
	form = vehiculoSoatForm()
	if request.method == "POST":
		form = vehiculoSoatForm(request.POST)
	return render(request, 'vehiculo_soat.html', {'forms': form})

class ReporteSoatPDFView(PDFTemplateView):
	template_name = "pdf_vehiculo_soat.html"

	def get_context_data(self, **kwargs):
		context = super(ReporteSoatPDFView, self).get_context_data(**kwargs)
		fecha_in = self.kwargs['fecha_in']
		fecha_fin = self.kwargs['fecha_fin']
		vehiculo_data = vehiculoModel.objects.filter(soat__range = [fecha_in, fecha_fin]).order_by('soat')
		context['vehiculo_data'] = vehiculo_data
		context['fecha_hoy'] = datetime.datetime.now().date()
		return context

def soat(request):
	now = datetime.datetime.now().date()
	soat = vehiculoModel.objects.filter(soat__lte = now).order_by('soat')
	return render(request, 'soat.html', {'soat': soat})