from datetime import datetime

from django.db import models

from vehiculos.models import vehiculoModel
from articulos_servicios.models import servicioModel
from maestros.models import mecanicoModel


class ordenServicioModel(models.Model):
	vehiculo = models.ForeignKey(vehiculoModel,null=False,blank=False)
	fecha = models.DateTimeField(null=False,blank=False,default=datetime.now)
	state = models.PositiveIntegerField(default = 1)

	def __str__(self):
		return u'%s' % (self.pk)

	def __unicode__(self):
		return u'%s' % (self.pk)

class ordenServicioDetalleModel(models.Model):
	servicio = models.ForeignKey(servicioModel,null=False,blank=False)
	cantidad = models.PositiveIntegerField(null=True,blank=True)
	valorUnitario = models.PositiveIntegerField(null=True,blank=True,verbose_name='V. Unitario')
	valorTotal = models.PositiveIntegerField(null=True,blank=True, verbose_name='V. Total')
	mecanico = models.ForeignKey(mecanicoModel,null=True,blank=True)
	ordenServicio = models.ForeignKey(ordenServicioModel,null=False,blank=False)
	time = models.TimeField(auto_now = False, null = True, blank = True)
	def __str__(self):
		return u'%s - %s' % (self.ordenServicio, self.pk)

	def __unicode__(self):
		return u'%s - %s' % (self.ordenServicio, self.pk)
