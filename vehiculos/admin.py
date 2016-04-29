from django.contrib import admin

from vehiculos.models import vehiculoModel, tipoVehiculoModel, MarcaModel


admin.site.register(vehiculoModel)
admin.site.register(tipoVehiculoModel)
admin.site.register(MarcaModel)

