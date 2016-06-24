from django.db import models
from django.contrib.auth.models import User

class usuariosModel(models.Model):
	usuario = models.OneToOneField(User, primary_key=True)
	cedula = models.PositiveIntegerField(null=True, blank=True)
	celular = models.PositiveIntegerField(null=True, blank=True)

	def __str__(self):
		return u'%s' % (self.usuario)

	def __unicode__(self):
		return u'%s' % (self.usuario)