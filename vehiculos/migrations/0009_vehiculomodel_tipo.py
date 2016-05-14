# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0008_auto_20160513_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculomodel',
            name='tipo',
            field=models.ForeignKey(blank=True, to='vehiculos.tipoVehiculoModel', null=True),
        ),
    ]
