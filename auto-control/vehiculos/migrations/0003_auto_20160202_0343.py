# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0002_vehiculomodel_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculomodel',
            name='tipo',
            field=models.ForeignKey(blank=True, to='vehiculos.tipoVehiculoModel', null=True),
        ),
    ]
