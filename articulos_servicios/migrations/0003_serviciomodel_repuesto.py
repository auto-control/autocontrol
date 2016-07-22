# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos_servicios', '0002_auto_20160720_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviciomodel',
            name='repuesto',
            field=models.BooleanField(default=False),
        ),
    ]
