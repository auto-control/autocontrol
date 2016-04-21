from django.db import models

class clienteModel(models.Model):

	"""Modelo Cliente"""
	nombre = models.CharField(max_length=35)
	apellido = models.CharField(max_length=35)
	documento = models.CharField(max_length=20)
	telefono = models.CharField(max_length=20, blank=True, null=True)
	celular = models.CharField(max_length=50)
	direccion = models.CharField(max_length=50, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)

	def __str__(self):
		return u'%s %s' % (self.nombre, self.apellido)

	def __unicode__(self):
		return u'%s %s' % (self.nombre, self.apellido)
