from django import forms

from clientes.models import clienteModel


class clienteModelForm(forms.ModelForm):
	class Meta:
		model = clienteModel
		fields = '__all__'
		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form-control col-10'}),
			'apellido': forms.TextInput(attrs={'class': 'form-control col-10'}),
			'telefono': forms.TextInput(attrs={'class': 'form-control col-10'}),
			'celular': forms.TextInput(attrs={'class': 'form-control col-10'}),
			'direccion': forms.TextInput(attrs={'class': 'form-control col-10'}),
			'email': forms.EmailInput(attrs={'class': 'form-control col-10'})
		}
