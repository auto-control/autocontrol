# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin


from maestros.models import mecanicoModel
from maestros.forms import mecanicoModelForm

class listMecanicosView(ListView):
	template_name = 'list_mecanicos.html'
	model = mecanicoModel
	context_object_name = 'mecanicos'

class createMecanicoView(SuccessMessageMixin, CreateView):
	template_name = 'create_mecanicos.html'
	form_class = mecanicoModelForm
	success_url = '/mecanicos'
	success_message = 'Se añadio con exito el Mecánico'
