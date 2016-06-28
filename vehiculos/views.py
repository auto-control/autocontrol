# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView, CreateView, ListView, UpdateView


from app.utils import get_or_none
from django.core import serializers
from django.views.generic import DetailView
from ordenes_servicios.models import ordenServicioModel
from vehiculos.models import *
from vehiculos.forms import buscarVehiculoHistorialForm, vehiculoModelForm


def historialVehiculo(request):
	form = buscarVehiculoHistorialForm()
	message = ''
	if request.method == 'POST':
		form = buscarVehiculoHistorialForm(request.POST)
		if form.is_valid():
			placa = form.cleaned_data['placa']
			vehiculo = get_or_none(vehiculoModel, placa=placa)
			if vehiculo is not None:
				url = u'%s/%s' % ('/historial', placa)
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

	#def get_object(self, queryset=None):
	#	pk = self.kwargs.get(self.pk_url_kwarg)
	#	if pk is None:
	#		raise AttributeError("Error")
	#	else:
	#		raise AttributeError("Sin Error")
#
	#	return obj

		# obj = super(historialVehiculoDetail, self).get_object(queryset=None)
		# if obj is None:
		#	 return obj
		# else:
		#	 return obj

