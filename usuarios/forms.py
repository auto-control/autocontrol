# -*- encoding: utf-8 -*-
from django import forms

class UserForm(forms.Form):
	email = forms.EmailField(label = 'Correo electrónico', widget = forms.EmailInput(attrs = {'class': 'form-control', 'required': True}))