# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes_servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenserviciomodel',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
