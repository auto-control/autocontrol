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
            name='detail',
            field=models.CharField(default=b'-', max_length=1000),
        ),
    ]
