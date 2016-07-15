# -*- encoding: utf-8 -*-
from django import forms
from clientes.models import clienteModel
from vehiculos.models import *
import datetime

class vehiculoModelForm(forms.ModelForm):
	class Meta:
		model = vehiculoModel
		fields = '__all__'
		widgets = {
			'placa': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'XXX111', 'max_length': 10, 'title': 'XXX000(Mayusculas)', 'pattern': '[A-Z]{3}[0-9]{3}'}),
			'linea': forms.TextInput(attrs={'class': 'form-control', 'max_length': 50, 'required': True,}),
			'kilometraje_actual': forms.TextInput(attrs={'class': 'form-control', 'max_length': 10, 'required': True,}),
			'soat': forms.TextInput(attrs={'class': 'form-control', 'type': 'date', 'required': True,}),
			'cilindraje': forms.TextInput(attrs={'class': 'form-control number', 'pattern': '[0-9]{1,9}', 'title': 'Solo dato numerico', 'required': True,}),
			'modelo': forms.TextInput(attrs={'class': 'form-control number', 'pattern': '[0-9]{4}', 'title': 'Solo dato numerico', 'required': True,}),
			'linea': forms.Select(attrs={'class': 'form-control', 'disabled': True}),
		}

	def __init__(self, *args, **kwargs):
		super(vehiculoModelForm, self).__init__(*args, **kwargs)
		self.fields['marca'] = forms.ModelChoiceField(queryset = MarcaModel.objects.all().order_by('marca'), widget = forms.Select(attrs = {'class': 'form-control chosen'}), required = False)
		self.fields['categoria'] = forms.ModelChoiceField(queryset = tipoVehiculoModel.objects.all().order_by('nombre'), widget = forms.Select(attrs = {'class': 'form-control chosen'}), required = True)
		self.fields['cliente'] = forms.ModelChoiceField(queryset = clienteModel.objects.all().order_by('nombre'), widget = forms.Select(attrs = {'class': 'form-control chosen', 'required': True}))

	def clean_placa(self):
		placa = self.cleaned_data['placa']
		if vehiculoModel.objects.filter(placa = placa).exclude(pk = self.instance.id).exists():
			raise forms.ValidationError("La placa ya se encuentra registrada")
		return placa

	def clean_soat(self):
		soat = self.cleaned_data['soat']
		now = datetime.datetime.now().date()
		before = now - datetime.timedelta(days = 365)
		print before
		if soat < before:
			raise forms.ValidationError("Fecha incorrecta. Maximo un año de vencimiento")
		return soat

	def clean_modelo(self):
		modelo = self.cleaned_data['modelo']
		if int(modelo) < 1900:
			raise forms.ValidationError("Modelo incorrecto.")
		return modelo

class buscarVehiculoHistorialForm(forms.Form):
	placa = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))

class vehiculoOrden(forms.ModelForm):
	class Meta:
		model = vehiculoModel
		exclude = ['cilindraje', 'cliente']
		widgets = {
			'placa': forms.TextInput(attrs={'class': 'form-control'}),
			'marca': forms.TextInput(attrs={'class': 'form-control'}),
			'clase': forms.Select(attrs={'class': 'form-control'}),
		}

class vehiculoSoatForm(forms.Form):
	fecha_in = forms.CharField(label = "Fecha de inicio", widget = forms.TextInput(attrs = {'class': 'form-control datepicker', 'required': True}))
	fecha_fin = forms.CharField(label = "Fecha Final", widget = forms.TextInput(attrs = {'class': 'form-control datepicker', 'required': True}))