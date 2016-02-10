# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes_servicios', '0004_auto_20160202_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenserviciodetallemodel',
            name='cantidad',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
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
