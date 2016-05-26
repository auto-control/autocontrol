# -*- encoding: utf-8 -*-
from django import forms

from clientes.models import clienteModel


class clienteModelForm(forms.ModelForm):
	class Meta:
		model = clienteModel
		fields = '__all__'
		widgets = {
			'nombre': forms.TextInput(attrs={'required': True, 'class': 'form-control', 'maxlength': 35, 'pattern': '[A-Za-z-ñÑáéíóúÁÉÍÓÚ ]+', 'title': 'Digite solo letras'}),
			'apellido': forms.TextInput(attrs={'required': True, 'class': 'form-control', 'maxlength': 35, 'pattern': '[A-Za-z-ñÑáéíóúÁÉÍÓÚ ]+', 'title': 'Digite solo letras'}),
			'documento': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]{1,12}', 'title': 'Digite solo numeros'}),
			'fnaci': forms.DateInput(attrs={'class': 'form-control'}),
			'telefono': forms.TextInput(attrs={'placeholder': 'XXXXXXXXX', 'class': 'form-control', 'maxlength': 10, 'pattern': '[0-9]{1,10}', 'title': 'Digite solo numeros'}),
			'celular': forms.TextInput(attrs={'required': True, 'placeholder': 'XXXXXXXXX', 'class': 'form-control', 'maxlength': 10, 'pattern': '[0-9]{1,10}', 'title': 'Digite solo numeros'}),
			'direccion': forms.TextInput(attrs={'placeholder': 'XXXXXXXX', 'class': 'form-control'}),
			'email': forms.EmailInput(attrs={'placeholder': 'ejemplo@ejemplo.com', 'required': True, 'class': 'form-control'})
		}
