from django import forms

from vehiculos.models import vehiculoModel

class vehiculoModelForm(forms.ModelForm):
	class Meta:
		model = vehiculoModel
		fields = '__all__'

class buscarVehiculoHistorialForm(forms.Form):
	placa = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))

class vehiculoOrden(forms.ModelForm):
	class Meta:
		model = vehiculoModel
		exclude = ['cilindraje', 'cliente']
		widgets = {
			'placa': forms.TextInput(attrs={'class': 'form-control'}),
			'marca': forms.TextInput(attrs={'class': 'form-control'}),
			'tipo': forms.Select(attrs={'class': 'form-control'}),
		}