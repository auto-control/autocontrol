# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientemodel',
            name='apellido',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='clientemodel',
            name='nombre',
            field=models.CharField(max_length=35),
        ),
    ]
