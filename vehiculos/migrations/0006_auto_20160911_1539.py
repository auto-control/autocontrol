# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0005_auto_20160823_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculomodel',
            name='foto_chasis',
            field=models.ImageField(default=b'img/none.jpg', null=True, upload_to=b'img/vehiculo/', blank=True),
        ),
        migrations.AddField(
            model_name='vehiculomodel',
            name='foto_motor',
            field=models.ImageField(default=b'img/none.jpg', null=True, upload_to=b'img/vehiculo/', blank=True),
        ),
    ]
