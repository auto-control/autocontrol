from django.db import models

from clientes.models import clienteModel


class tipoVehiculoModel(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return u'%s' % (self.nombre)

	def __unicode__(self):
		return u'%s' % (self.nombre)

class vehiculoModel(models.Model):
	placa = models.CharField(max_length=10, primary_key=True, null=False, blank=False)
	cilindraje = models.IntegerField(null=True, blank=True)
	marca = models.CharField(max_length=50, null=True, blank=True)
	tipo = models.ForeignKey(tipoVehiculoModel, null=True, blank=True)
	cliente = models.ForeignKey(clienteModel, null=False, blank=False)

	def __str__(self):
		return u'%s' % (self.placa)

	def __unicode__(self):
		return u'%s' % (self.placa)

