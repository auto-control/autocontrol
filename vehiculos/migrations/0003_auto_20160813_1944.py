# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0002_auto_20160812_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculomodel',
            name='foto',
            field=models.ImageField(default=b'img/none.jpg', null=True, upload_to=b'img/vehiculo/', blank=True),
        ),
    ]
