# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculomodel',
            name='foto',
            field=models.ImageField(default=b'none.jpg', upload_to=b'img/vehiculo/'),
        ),
    ]
