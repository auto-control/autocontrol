# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarcaModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marca', models.CharField(max_length=50)),
            ],
        ),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('placa', models.CharField(max_length=10)),
                ('cilindraje', models.IntegerField(null=True, blank=True)),
                ('clase', models.CharField(max_length=50, null=True, blank=True)),
                ('kilometraje_actual', models.CharField(max_length=10, null=True, blank=True)),
                ('soat', models.DateField(null=True, blank=True)),
                ('foto', models.ImageField(default=b'img/none.jpg', upload_to=b'img/vehiculo/')),
                ('cliente', models.ForeignKey(to='clientes.clienteModel')),
                ('marca', models.ForeignKey(blank=True, to='vehiculos.MarcaModel', null=True)),
                ('tipo', models.ForeignKey(blank=True, to='vehiculos.tipoVehiculoModel', null=True)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
