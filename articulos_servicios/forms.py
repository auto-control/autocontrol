from django import forms

from articulos_servicios.models import servicioModel

class servicioModelForm(forms.ModelForm):
	class Meta:
		model = servicioModel
		fields = '__all__'
		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form-control col-10'}),
			'valor': forms.NumberInput(attrs={'class': 'form-control col-10'}),
			'time': forms.TextInput(attrs={'class': 'form-control col-10'}),
			'grupo': forms.Select(attrs={'class': 'form-control col-10'}),
		}