# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes_servicios', '0005_auto_20160208_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenserviciodetallemodel',
            name='cantidad',
            field=models.PositiveIntegerField(),
        ),
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
    ]
