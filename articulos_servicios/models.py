from django.db import models

class grupoServicioModel(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return u'%s' % (self.nombre)

	def __unicode__(self):
		return u'%s' % (self.nombre)

class servicioModel(models.Model):
	nombre = models.CharField(max_length=100)
	valor =  models.PositiveIntegerField()
	servicio = models.BooleanField(default = True)
	grupo = models.ForeignKey(grupoServicioModel, blank = True, null = True)
	time = models.TimeField(default = '0:00:00')
	detail = models.CharField(max_length = 1000, default = '-')

	def __str__(self):
		return u'%s' % (self.nombre)

	def __unicode__(self):
		return u'%s' % (self.nombre)