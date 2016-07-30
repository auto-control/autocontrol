from django.db import models
from django.contrib.auth.models import User

class tipoUsuario(models.Model):
	nombre_tipo = models.CharField(max_length=20)

	def __str__(self):
		return u'%s' % (self.nombre_tipo)

	def __unicode__(self):
		return u'%s' % (self.nombre_tipo)

class usuariosModel(models.Model):
	usuario = models.OneToOneField(User, primary_key=True)
	tipoUsuario = models.ForeignKey(tipoUsuario, null=True, blank=True)

	def __str__(self):
		return u'%s' % (self.usuario)

	def __unicode__(self):
		return u'%s' % (self.usuario)