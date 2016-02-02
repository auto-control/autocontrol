# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos_servicios', '0001_initial'),
        ('vehiculos', '0001_initial'),
        ('maestros', '0002_mecanicomodel_activo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ordenServicioDetalleModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.PositiveIntegerField()),
                ('valorUnitario', models.PositiveIntegerField()),
                ('valorTotal', models.PositiveIntegerField()),
                ('mecanico', models.ForeignKey(to='maestros.mecanicoModel')),
                ('servicio', models.ForeignKey(to='articulos_servicios.servicioModel')),
            ],
        ),
        migrations.CreateModel(
            name='ordenServicioModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField()),
                ('ordenDetalle', models.ForeignKey(to='ordenes_servicios.ordenServicioDetalleModel')),
                ('vehiculo', models.ForeignKey(to='vehiculos.vehiculoModel')),
            ],
        ),
    ]
