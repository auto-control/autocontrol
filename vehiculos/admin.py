from django.contrib import admin

from vehiculos.models import vehiculoModel, tipoVehiculoModel


admin.site.register(vehiculoModel)
admin.site.register(tipoVehiculoModel)
