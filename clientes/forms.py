# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from clientes.models import clienteModel


class clienteModelForm(forms.ModelForm):
	class Meta:
		model = clienteModel
		fields = '__all__'
		exclude = {'cuenta'}
		widgets = {
			'nombre': forms.TextInput(attrs={'required': True, 'class': 'form-control', 'maxlength': 35, 'title': 'Digite solo letras'}),
			'apellido': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 35, 'title': 'Digite solo letras'}),
			'documento': forms.TextInput(attrs={'class': 'form-control'}),
			'fnaci': forms.TextInput(attrs={'class': 'form-control datepicker'}),
			'telefono': forms.TextInput(attrs={'placeholder': 'XXXXXXXXX', 'class': 'form-control', 'maxlength': 10, 'pattern': '[0-9]{1,10}', 'title': 'Digite solo numeros'}),
			'celular': forms.TextInput(attrs={'placeholder': 'XXXXXXXXX', 'class': 'form-control', 'maxlength': 10, 'pattern': '[0-9]{1,10}', 'title': 'Digite solo numeros'}),
			'direccion': forms.TextInput(attrs={'placeholder': 'XXXXXXXX', 'class': 'form-control'}),
			'email': forms.EmailInput(attrs={'placeholder': 'ejemplo@ejemplo.com', 'class': 'form-control'})
		}
		labels = {
			'fnaci': 'Fecha de nacimiento'
		}

	def clean_documento(self):
		documento = self.cleaned_data['documento']
		if documento != '':
			if clienteModel.objects.filter(documento = documento).exclude(pk = self.instance.pk).count() > 0:
				raise forms.ValidationError("El No. de documento ya está registrado.")
		return documento

	def clean_telefono(self):
		telefono = self.cleaned_data['telefono']
		if telefono != '':
			if clienteModel.objects.filter(telefono = telefono).exclude(pk = self.instance.pk).count() > 0 and telefono != "":
				raise forms.ValidationError("El No. de telefono ya está registrado.")
		return telefono

	def clean_celular(self):
		celular = self.cleaned_data['celular']
		if celular != '':
			if clienteModel.objects.filter(celular = celular).exclude(pk = self.instance.pk).count() > 0:
				raise forms.ValidationError("El No. de celular ya está registrado.")
		return celular

	def clean_email(self):
		email = self.cleaned_data['email']
		if email != '':
			if clienteModel.objects.filter(email = email).exclude(pk = self.instance.pk).count() > 0:
				raise forms.ValidationError("El email ya está registrado.")
		return email
