# -*- encoding: utf-8 -*-
from django import forms
from maestros.models import mecanicoModel


class mecanicoModelForm(forms.ModelForm):
	class Meta:
		model = mecanicoModel
		fields = '__all__'
		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form-control col-10'}),
			'apellido': forms.TextInput(attrs={'class': 'form-control col-10'}),
			'documento': forms.TextInput(attrs={'class': 'form-control col-10', 'pattern': '[0-9]{1,12}', 'title': 'Digite solo numeros'}),
			'fnaci': forms.DateInput(attrs={'class': 'form-control col-10', 'max': '1998-12-31', 'type': 'date'}),
			'telefono': forms.TextInput(attrs={'class': 'form-control col-10'}),
			'celular': forms.TextInput(attrs={'class': 'form-control col-10'}),
			'direccion': forms.TextInput(attrs={'class': 'form-control col-10'}),
		}
		labels = {
			'fnaci': 'Fecha de nacimiento'
		}

	def clean_documento(self):
		documento = self.cleaned_data['documento']
		if mecanicoModel.objects.filter(documento = documento).count() > 0:
			raise forms.ValidationError("El No. de documento ya está registrado.")
		return documento

	def clean_celular(self):
		celular = self.cleaned_data['celular']
		if mecanicoModel.objects.filter(celular = celular).count() > 0:
			raise forms.ValidationError("El No. de celular ya está registrado.")
		return celular

	def clean_telefono(self):
		telefono = self.cleaned_data['telefono']
		if mecanicoModel.objects.filter(telefono = telefono).count() > 0:
			raise forms.ValidationError("El No. de telefono ya está registrado.")
		return telefono