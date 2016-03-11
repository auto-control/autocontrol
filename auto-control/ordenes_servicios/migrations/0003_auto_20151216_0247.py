# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes_servicios', '0002_auto_20151216_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenserviciodetallemodel',
            name='mecanico',
            field=models.ForeignKey(blank=True, to='maestros.mecanicoModel', null=True),
        ),
    ]
