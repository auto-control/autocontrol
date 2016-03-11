from ordenes_servicios.models import *
from maestros.models import *
from django import template
from datetime import datetime, time, timedelta
register = template.Library()
from django.db.models import Sum

@register.filter
def time_tot(value):
	time = ''
	mecanico = mecanicoModel.objects.get(pk = value)
	servicio_mecanico = ordenServicioDetalleModel.objects.filter(mecanico = mecanico)
	sum_tot = datetime.strptime('00:00:00', '%H:%M:%S')
	for hour in servicio_mecanico:
		time_service =  hour.servicio.time
		hour = time_service.hour
		minute = time_service.minute
		sum_tot = sum_tot + timedelta(hours = hour, minutes = minute)
	if sum_tot.minute > 0:
		time = ' y '+str(sum_tot.minute)+' minutos'
	return 'Tiempo de carga: '+str(sum_tot.hour)+' horas'+time