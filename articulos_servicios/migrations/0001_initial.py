# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='grupoServicioModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='servicioModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('valor', models.PositiveIntegerField()),
                ('servicio', models.BooleanField(default=True)),
                ('time', models.TimeField(default=b'0:00:00')),
                ('detail', models.CharField(default=b'-', max_length=1000)),
                ('grupo', models.ForeignKey(blank=True, to='articulos_servicios.grupoServicioModel', null=True)),
            ],
        ),
    ]
