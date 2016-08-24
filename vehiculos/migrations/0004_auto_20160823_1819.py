# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0003_auto_20160813_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculomodel',
            name='n_chasis',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vehiculomodel',
            name='n_motor',
            field=models.CharField(max_length=50),
        ),
    ]
