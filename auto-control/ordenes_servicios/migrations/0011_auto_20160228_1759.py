# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes_servicios', '0010_auto_20160225_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenserviciomodel',
            name='fecha',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
