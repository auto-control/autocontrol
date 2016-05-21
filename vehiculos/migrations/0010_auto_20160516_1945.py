# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0009_vehiculomodel_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculomodel',
            name='kilometraje_actual',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='vehiculomodel',
            name='soat',
            field=models.DateField(null=True, blank=True),
        ),
    ]
