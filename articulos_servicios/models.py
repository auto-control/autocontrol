from django.db import models

class grupoServicioModel(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return u'%s' % (self.nombre)

	def __unicode__(self):
		return u'%s' % (self.nombre)

class servicioModel(models.Model):
	servicio = models.BooleanField(default = True)
	repuesto = models.BooleanField(default = False)
	nombre = models.CharField(max_length=100)
	referencia = models.CharField(max_length = 15, blank = True, null = True)
	valor =  models.PositiveIntegerField()
	grupo = models.ForeignKey(grupoServicioModel, blank = True, null = True)
	time = models.TimeField(default = '0:00:00', blank = True, null = True)
	detail = models.CharField(max_length = 1000, default = '-')
	fecha_vencimiento = models.DateField(blank = True, null = True)

	def __str__(self):
		return u'%s' % (self.nombre)

	def __unicode__(self):
		return u'%s' % (self.nombre)