# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0003_auto_20160329_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculomodel',
            name='foto',
            field=models.ImageField(default=b'img/none.png', upload_to=b'img/vehiculo/'),
        ),
    ]
