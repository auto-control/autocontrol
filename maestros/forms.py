# -*- encoding: utf-8 -*-
from django import forms
from maestros.models import mecanicoModel
from django.contrib.auth.models import User

class mecanicoModelForm(forms.ModelForm):
	class Meta:
		model = mecanicoModel
		fields = '__all__'
		exclude = {'cuenta'}
		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form-control col-md-10'}),
			'apellido': forms.TextInput(attrs={'class': 'form-control col-md-10'}),
			'documento': forms.TextInput(attrs={'class': 'form-control col-md-10', 'pattern': '[0-9]{1,12}', 'title': 'Digite solo numeros'}),
			'fnaci': forms.DateInput(attrs={'class': 'form-control col-md-10', 'max': '1998-12-31', 'type': 'date'}),
			'telefono': forms.TextInput(attrs={'class': 'form-control col-md-10'}),
			'celular': forms.TextInput(attrs={'class': 'form-control col-md-10'}),
			'direccion': forms.TextInput(attrs={'class': 'form-control col-md-10'}),
		}
		labels = {
			'fnaci': 'Fecha de nacimiento'
		}

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email = email).exclude(pk = self.instance.cuenta.usuario.pk).count() > 0:
			raise forms.ValidationError("El email ya está registrado.")
		return email

	def clean_documento(self):
		documento = self.cleaned_data['documento']
		if mecanicoModel.objects.filter(documento = documento).exclude(pk = self.instance.pk).count() > 0:
			raise forms.ValidationError("El No. de documento ya está registrado")
		return documento

	def clean_celular(self):
		celular = self.cleaned_data['celular']
		if mecanicoModel.objects.filter(celular = celular).exclude(pk = self.instance.pk).count() > 0:
			raise forms.ValidationError("El No. de celular ya está registrado")
		return celular

	def clean_telefono(self):
		telefono = self.cleaned_data['telefono']
		if mecanicoModel.objects.filter(telefono = telefono).exclude(pk = self.instance.pk).count() > 0:
			raise forms.ValidationError("El No. de telefono ya está registrado")
		return telefono

	def __init__(self, *args, **kwargs):
		data = kwargs['instance']
		super(mecanicoModelForm, self).__init__(*args, **kwargs)
		if data:
			data = data.cuenta.usuario.email
		else:
			data = ''
		self.fields['email'] = forms.EmailField(label = "Correo electronico", widget = forms.TextInput(attrs = {'class': 'form-control col-md-10', 'value': data, 'required': True}))