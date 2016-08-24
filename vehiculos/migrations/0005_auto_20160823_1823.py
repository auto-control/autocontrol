# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0004_auto_20160823_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculomodel',
            name='n_chasis',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='vehiculomodel',
            name='n_motor',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
