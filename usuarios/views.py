from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import login

from app.utils import get_or_none
from usuarios.models import usuariosModel
from usuarios.forms import loginForm

class loginView(FormView):
	# parametros de clase 
	form_class = loginForm
	template_name = 'login.html'
	success_url = '/'

	def form_valid(self, form):
		perfil = get_or_none(usuariosModel, usuario=form.user_cache)
		if perfil is not None:
			login(self.request, form.user_cache)
		else:
			form.add_error(None, 'Lo sentimos este usuario no esta registrado')
			return self.form_invalid(form)
		return super(loginView, self).form_valid(form)

	def get_success_url(self):
		if self.request.GET.get('next'):
			return self.request.GET.get('next')
		else:
			return super(loginView, self).get_success_url()

	def get_context_data(self, **kwargs):
		context = super(loginView, self).get_context_data(**kwargs)
		context['next'] = self.request.GET.get('next')
		return context