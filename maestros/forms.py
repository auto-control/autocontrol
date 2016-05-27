from django import forms


from maestros.models import mecanicoModel


class mecanicoModelForm(forms.ModelForm):
	class Meta:
		model = mecanicoModel
		fields = '__all__'
		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form-control col-10'}),
			'apellido': forms.TextInput(attrs={'class': 'form-control col-10'}),
			'documento': forms.TextInput(attrs={'class': 'form-control col-10', 'pattern': '[0-9]{1,12}', 'title': 'Digite solo numeros'}),
			'fnaci': forms.DateInput(attrs={'class': 'form-control col-10', 'max': '1998-12-31', 'type': 'date'}),
			'telefono': forms.TextInput(attrs={'class': 'form-control col-10'}),
			'celular': forms.TextInput(attrs={'class': 'form-control col-10'}),
			'direccion': forms.TextInput(attrs={'class': 'form-control col-10'}),
		}
		labels = {
			'fnaci': 'Fecha de nacimiento'
		}