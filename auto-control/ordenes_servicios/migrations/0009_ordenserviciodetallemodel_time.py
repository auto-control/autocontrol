# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes_servicios', '0008_auto_20160214_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenserviciodetallemodel',
            name='time',
            field=models.TimeField(default=0),
        ),
    ]
