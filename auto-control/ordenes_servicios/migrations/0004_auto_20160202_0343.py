# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes_servicios', '0003_auto_20151216_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenserviciodetallemodel',
            name='valorTotal',
            field=models.PositiveIntegerField(verbose_name=b'V. Total'),
        ),
        migrations.AlterField(
            model_name='ordenserviciodetallemodel',
            name='valorUnitario',
            field=models.PositiveIntegerField(verbose_name=b'V. Unitario'),
        ),
        migrations.AlterField(
            model_name='ordenserviciomodel',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
