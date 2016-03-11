# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes_servicios', '0007_auto_20160214_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenserviciodetallemodel',
            name='valorTotal',
            field=models.PositiveIntegerField(null=True, verbose_name=b'V. Total', blank=True),
        ),
        migrations.AlterField(
            model_name='ordenserviciodetallemodel',
            name='valorUnitario',
            field=models.PositiveIntegerField(null=True, verbose_name=b'V. Unitario', blank=True),
        ),
    ]
