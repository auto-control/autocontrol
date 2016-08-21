# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20160813_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientemodel',
            name='apellido',
            field=models.CharField(max_length=35, null=True, blank=True),
        ),
    ]
