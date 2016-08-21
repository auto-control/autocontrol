from django.db import models
from usuarios.models import usuariosModel

class clienteModel(models.Model):

	"""Modelo Cliente"""
	cuenta = models.ForeignKey(usuariosModel, blank=True, null=True)
	nombre = models.CharField(max_length=35)
	apellido = models.CharField(max_length=35, blank=True, null=True)
	documento = models.CharField(max_length=20,blank=True, null=True)
	fnaci = models.DateField(blank=True, null=True)
	telefono = models.CharField(max_length=20, blank=True, null=True)
	celular = models.CharField(max_length=50,blank=True, null=True)
	direccion = models.CharField(max_length=50, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)

	def __str__(self):
		return u'%s %s' % (self.nombre, self.apellido)

	def __unicode__(self):
		return u'%s %s' % (self.nombre, self.apellido)
