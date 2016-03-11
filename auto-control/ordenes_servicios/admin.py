from django.contrib import admin

from ordenes_servicios.models import ordenServicioModel, ordenServicioDetalleModel

admin.site.register(ordenServicioModel)
admin.site.register(ordenServicioDetalleModel)