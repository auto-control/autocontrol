from django import forms

from articulos_servicios.models import servicioModel

class servicioModelForm(forms.ModelForm):
	class Meta:
		model = servicioModel
		fields = '__all__'
		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form-control'}),
			'valor': forms.NumberInput(attrs={'class': 'form-control', 'value': 0, 'min': 0}),
			'time': forms.TextInput(attrs={'class': 'form-control servicio'}),
			'grupo': forms.Select(attrs={'class': 'form-control servicio'}),
			'detail': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
			'fecha_vencimiento': forms.TextInput(attrs={'type': 'date', 'class': 'form-control articulo'}),
			'referencia': forms.TextInput(attrs={'class': 'form-control articulo'}),
		}
		labels = {
			'time': 'Tiempo',
			'detail': 'Detalle',
			'fecha_vencimiento': 'Fecha de vencimiento'
		}