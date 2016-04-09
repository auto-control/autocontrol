from django import forms

from clientes.models import clienteModel


class clienteModelForm(forms.ModelForm):
	class Meta:
		model = clienteModel
		fields = '__all__'
		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form-control'}),
			'documento': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]{1,12}'}),
			'apellido': forms.TextInput(attrs={'class': 'form-control'}),
			'telefono': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]{1,10}'}),
			'celular': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]{1,10}'}),
			'direccion': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.EmailInput(attrs={'class': 'form-control'})
		}
