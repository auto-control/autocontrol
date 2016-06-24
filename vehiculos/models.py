# -*- encoding: utf-8 -*-
from django.db import models

from clientes.models import clienteModel


class MarcaModel(models.Model):
	marca = models.CharField(max_length=50)

	def __str__(self):
		return u'%s' % (self.marca)

	def __unicode__(self):
		return u'%s' % (self.marca)


class tipoVehiculoModel(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return u'%s' % (self.nombre)

	def __unicode__(self):
		return u'%s' % (self.nombre)

class vehiculoModel(models.Model):
	placa = models.CharField(max_length=10, null=False, blank=False)
	cilindraje = models.IntegerField(null=True, blank=True)
	marca = models.ForeignKey(MarcaModel, null=True, blank=True)
	#clase = models.CharField(max_length=50, null=True, blank=True)
	linea = models.CharField(max_length=50, null=True, blank=True)
	kilometraje_actual = models.CharField(max_length = 10, null = True, blank = True)
	soat = models.DateField(auto_now = False, null = True, blank = True)
	#tipo = models.ForeignKey(tipoVehiculoModel, null=True, blank=True)
	categoria = models.ForeignKey(tipoVehiculoModel, null=True, blank=True)
	modelo = models.IntegerField(null=True, blank=True)
	cliente = models.ForeignKey(clienteModel, null=False, blank=False)
	foto = models.ImageField(upload_to = 'img/vehiculo/', default = 'img/none.jpg')

	def __str__(self):
		return str(self.placa)

	def __unicode__(self):
		return str(self.placa)

	class Meta:
		ordering = ['-pk']

