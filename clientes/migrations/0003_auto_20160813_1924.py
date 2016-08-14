# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_clientemodel_cuenta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientemodel',
            name='celular',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clientemodel',
            name='documento',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
