from django.db import models

class empresaModel(models.Model):


	nit = models.CharField(max_length=35, null= False, blank=False)
	nombre = models.CharField(max_length=35, null=False, blank=False)
	representanteLegal = models.CharField(max_length=35, null=False, blank=False)
	telefono = models.IntegerField(blank=True, null=True)
	pbx = models.CharField(max_length=10, blank=True, null=True)
	direccion = models.CharField(max_length=50, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	numeracionAutorizada = models.IntegerField(null=False, blank=False)
    #logo = models.imageField()
	
	def __str__(self):
		return u'%s ' % (self.nombre)

	def __unicode__(self):
		return u'%s ' % (self.nombre)
