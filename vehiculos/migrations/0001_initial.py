# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tipoVehiculoModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='vehiculoModel',
            fields=[
                ('placa', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('cilindraje', models.IntegerField(null=True, blank=True)),
                ('marca', models.CharField(max_length=50, null=True, blank=True)),
                ('foto', models.ImageField(default=b'img/none.jpg', upload_to=b'img/vehiculo/')),
                ('cliente', models.ForeignKey(to='clientes.clienteModel')),
                ('tipo', models.ForeignKey(blank=True, to='vehiculos.tipoVehiculoModel', null=True)),
            ],
        ),
    ]
