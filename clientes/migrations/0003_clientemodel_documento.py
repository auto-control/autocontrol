# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20151113_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientemodel',
            name='documento',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
