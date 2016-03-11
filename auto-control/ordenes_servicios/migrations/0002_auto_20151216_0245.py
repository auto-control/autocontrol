# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes_servicios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordenserviciomodel',
            name='ordenDetalle',
        ),
        migrations.AddField(
            model_name='ordenserviciodetallemodel',
            name='ordenServicio',
            field=models.ForeignKey(default=1, to='ordenes_servicios.ordenServicioModel'),
            preserve_default=False,
        ),
    ]
