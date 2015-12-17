from django.db import models

from vehiculos.models import vehiculoModel
from articulos_servicios.models import servicioModel
from maestros.models import mecanicoModel


class ordenServicioModel(models.Model):
	vehiculo = models.ForeignKey(vehiculoModel,null=False,blank=False)
	fecha = models.DateTimeField(null=False,blank=False)

	def __str__(self):
		return u'%s' % (self.pk)

	def __unicode__(self):
		return u'%s' % (self.pk)

class ordenServicioDetalleModel(models.Model):
	servicio = models.ForeignKey(servicioModel,null=False,blank=False)
	cantidad = models.PositiveIntegerField(null=False,blank=False)
	valorUnitario = models.PositiveIntegerField(null=False,blank=False)
	valorTotal = models.PositiveIntegerField(null=False,blank=False)
	mecanico = models.ForeignKey(mecanicoModel,null=True,blank=True)
	ordenServicio = models.ForeignKey(ordenServicioModel,null=False,blank=False)

	def __str__(self):
		return u'%s - %s' % (self.ordenServicio, self.pk)

	def __unicode__(self):
		return u'%s - %s' % (self.ordenServicio, self.pk)
