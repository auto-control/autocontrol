# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes_servicios', '0009_ordenserviciodetallemodel_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenserviciodetallemodel',
            name='time',
            field=models.TimeField(),
        ),
    ]
