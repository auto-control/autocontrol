from django.shortcuts import render
from django.views.generic import ListView

from maestros.models import mecanicoModel


class listMecanicosView(ListView):
	template_name = 'list_mecanicos.html'
	model = mecanicoModel
	context_object_name = 'mecanicos'