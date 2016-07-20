# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos_servicios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviciomodel',
            name='fecha_vencimiento',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='serviciomodel',
            name='referencia',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='serviciomodel',
            name='time',
            field=models.TimeField(default=b'0:00:00', null=True, blank=True),
        ),
    ]
