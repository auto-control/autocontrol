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
	servicio = models.BooleanField(default=True)
	grupo = models.ForeignKey(grupoServicioModel)

	def __str__(self):
		return u'%s' % (self.nombre)

	def __unicode__(self):
		return u'%s' % (self.nombre)