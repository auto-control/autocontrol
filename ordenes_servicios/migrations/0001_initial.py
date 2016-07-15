# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0001_initial'),
        ('maestros', '0001_initial'),
        ('articulos_servicios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ordenServicioDetalleModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.PositiveIntegerField(null=True, blank=True)),
                ('valorUnitario', models.PositiveIntegerField(null=True, verbose_name=b'V. Unitario', blank=True)),
                ('valorTotal', models.PositiveIntegerField(null=True, verbose_name=b'V. Total', blank=True)),
                ('time', models.TimeField(null=True, blank=True)),
                ('fecha', models.DateField(auto_now=True, null=True)),
                ('mecanico', models.ForeignKey(blank=True, to='maestros.mecanicoModel', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ordenServicioModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(default=datetime.datetime.now)),
                ('state', models.PositiveIntegerField(default=1)),
                ('vehiculo', models.ForeignKey(to='vehiculos.vehiculoModel')),
            ],
        ),
        migrations.AddField(
            model_name='ordenserviciodetallemodel',
            name='ordenServicio',
            field=models.ForeignKey(to='ordenes_servicios.ordenServicioModel'),
        ),
        migrations.AddField(
            model_name='ordenserviciodetallemodel',
            name='servicio',
            field=models.ForeignKey(to='articulos_servicios.servicioModel'),
        ),
    ]
