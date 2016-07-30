from django.db import models
from usuarios.models import usuariosModel

class mecanicoModel(models.Model):
	cuenta = models.ForeignKey(usuariosModel, blank=True, null=True)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	telefono = models.CharField(max_length=20, blank=True, null=True)
	celular = models.CharField(max_length=20)
	documento = models.CharField(max_length=20, blank=True, null=True)
	fnaci = models.DateField(blank=True, null=True)
	direccion = models.CharField(max_length=50, blank=True, null=True)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return u'%s %s' % (self.nombre, self.apellido)

	def __unicode__(self):
		return u'%s %s' % (self.nombre, self.apellido)