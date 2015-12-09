from django import forms


from maestros.models import mecanicoModel


class mecanicoModelForm(forms.ModelForm):
	class Meta:
		model = mecanicoModel
		fields = '__all__'
		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form-control col-10'}),
			'apellido': forms.TextInput(attrs={'class': 'form-control col-10'}),
			'telefono': forms.TextInput(attrs={'class': 'form-control col-10'}),
			'celular': forms.TextInput(attrs={'class': 'form-control col-10'}),
			'direccion': forms.TextInput(attrs={'class': 'form-control col-10'}),
		}