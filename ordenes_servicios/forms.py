from django import forms
from maestros.models import mecanicoModel
from datetime import datetime, time, timedelta
from articulos_servicios.models import servicioModel
from vehiculos.models import vehiculoModel
from ordenes_servicios.models import ordenServicioDetalleModel, ordenServicioModel

class vehiculoOrdenForm(forms.Form):
	placa = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class ordenServicioAutoForm(forms.Form):
	placa = forms.ChoiceField(label = "Placa del auto", choices = [('','Seleccione un Auto')]+[('ALL', 'Todos')]+[(x.placa, x.placa) for x in vehiculoModel.objects.all()], widget = forms.Select(attrs = {'class': 'form-control', 'required': True}))
	fecha_in = forms.CharField(label = "Fecha de inicio", widget = forms.TextInput(attrs = {'class': 'form-control datepicker', 'required': True}))
	fecha_fin = forms.CharField(label = "Fecha Final", widget = forms.TextInput(attrs = {'class': 'form-control datepicker', 'required': True}))

class ordenServicioMecanicoForm(forms.Form):
	mecanico = forms.ChoiceField(label = "Mecanico", choices = [('','Seleccione un Mecanico')]+[('ALL', 'Todos')]+[(x.pk, x.nombre+' '+x.apellido) for x in mecanicoModel.objects.all()], widget = forms.Select(attrs = {'class': 'form-control', 'required': True}))
	fecha_in = forms.CharField(label = "Fecha de inicio", widget = forms.TextInput(attrs = {'class': 'form-control datepicker', 'required': True}))
	fecha_fin = forms.CharField(label = "Fecha Final", widget = forms.TextInput(attrs = {'class': 'form-control datepicker', 'required': True}))

class ordenPorServicioForm(forms.Form):
	servicio = forms.ChoiceField(label = "Servicios", choices = [('','Seleccione un Servicio')]+[('ALL', 'Todos')]+[(x.pk, x.nombre) for x in servicioModel.objects.all()], widget = forms.Select(attrs = {'class': 'form-control', 'required': True}))
	fecha_in = forms.CharField(label = "Fecha de inicio", widget = forms.TextInput(attrs = {'class': 'form-control datepicker', 'required': True}))
	fecha_fin = forms.CharField(label = "Fecha Final", widget = forms.TextInput(attrs = {'class': 'form-control datepicker', 'required': True}))

class ordenServicioDetalle(forms.ModelForm):
	class Meta:
		model = ordenServicioDetalleModel
		exclude = ['ordenServicio']
		widgets = {
			'valorTotal': forms.NumberInput(attrs={'disabled' : 'disabled'})
		}

	def __init__(self, *args, **kwargs):
		service = kwargs.pop('service', None)
		detail_service = [x.servicio.pk for x in ordenServicioDetalleModel.objects.filter(ordenServicio = service)]
		super(ordenServicioDetalle, self).__init__(*args, **kwargs)
		self.fields['servicio'] = forms.ChoiceField(label = "Servicio/Articulo", choices = [('','Seleccione un Servicio')]+[(x.pk, x.nombre) for x in servicioModel.objects.exclude(pk__in = detail_service).distinct()], widget = forms.Select(attrs = {'class': 'form-control', 'required': True}))
		self.fields['mecanico'] = forms.ChoiceField(label = "Mecanico", choices = [('','Seleccione un Mecanico')]+[(x.pk, x.nombre) for x in mecanicoModel.objects.all()], widget = forms.Select(attrs = {'class': 'form-control', 'required': True}))

	def save(self):
		ordenServicio = ordenServicioModel.objects.get(pk = str(self.instance))
		servicio = servicioModel.objects.get(pk = self.cleaned_data.get('servicio'))
		mecanico = mecanicoModel.objects.get(pk = self.cleaned_data.get('mecanico'))
		detalle_orden = ordenServicioDetalleModel(servicio = servicio, mecanico = mecanico, time = get_time(servicio.time), ordenServicio = ordenServicio)
		detalle_orden.save()
		return detalle_orden

def get_time(time):
	time_service = datetime.strptime(str(time), '%H:%M:%S')
	time_now = datetime.now()
	time = time_now + timedelta(hours = time_service.hour, minutes = time_service.minute)
	return time