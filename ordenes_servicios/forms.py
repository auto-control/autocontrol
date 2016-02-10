from django import forms

from ordenes_servicios.models import ordenServicioDetalleModel

class vehiculoOrdenForm(forms.Form):
	placa = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class ordenServicioDetalle(forms.ModelForm):
	class Meta:
		model = ordenServicioDetalleModel
		exclude = ['ordenServicio', 'cantidad', 'valorUnitario', 'valorTotal']
		widgets = {
			'valorTotal': forms.NumberInput(attrs={'disabled' : 'disabled'})
		}