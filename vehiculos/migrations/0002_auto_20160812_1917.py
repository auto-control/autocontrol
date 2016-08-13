# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculomodel',
            name='n_chasis',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vehiculomodel',
            name='n_motor',
            field=models.IntegerField(default=0),
        ),
    ]
