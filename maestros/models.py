from django.db import models

class mecanicoModel(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	telefono = models.CharField(max_length=20, blank=True, null=True)
	celular = models.CharField(max_length=20)
	direccion = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return u'%s %s' % (self.nombre, self.apellido)

	def __unicode__(self):
		return u'%s %s' % (self.nombre, self.apellido)