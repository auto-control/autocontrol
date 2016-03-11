# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20151113_0135'),
        ('vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculomodel',
            name='cliente',
            field=models.ForeignKey(default=1, to='clientes.clienteModel'),
            preserve_default=False,
        ),
    ]
