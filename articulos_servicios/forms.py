from django import forms

from articulos_servicios.models import servicioModel

class servicioModelForm(forms.ModelForm):
	class Meta:
		model = servicioModel
		fields = '__all__'
		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form-control col-10'}),
			'valor': forms.NumberInput(attrs={'class': 'form-control col-10', 'step': '5000'}),
			'time': forms.TextInput(attrs={'class': 'form-control col-10'}),
			'grupo': forms.Select(attrs={'class': 'form-control col-10'}),
			'detail': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'})
		}
		labels = {
			'time': 'Tiempo',
			'detail': 'Detalle'
		}