from django import forms

from clientes.models import clienteModel


class clienteModelForm(forms.ModelForm):
	class Meta:
		model = clienteModel
		fields = '__all__'
		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 35, 'pattern': '[A-Za-z]', 'title': 'Digite solo letras'}),
			'documento': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]{1,12}', 'title': 'Digite solo numeros'}),
			'apellido': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 35, 'pattern': '[A-Za-z]', 'title': 'Digite solo numeros'}),
			'telefono': forms.TextInput(attrs={'placeholder': 'xxxxxxxxxx', 'class': 'form-control', 'maxlength': 10, 'pattern': '[0-9]{1,10}', 'title': 'Digite solo numeros'}),
			'celular': forms.TextInput(attrs={'placeholder': 'xxxxxxxxxx', 'class': 'form-control', 'maxlength': 10, 'pattern': '[0-9]{1,10}', 'title': 'Digite solo numeros'}),
			'direccion': forms.TextInput(attrs={'placeholder': 'xxxxxxx', 'class': 'form-control'}),
			'email': forms.EmailInput(attrs={'class': 'form-control'})
		}
