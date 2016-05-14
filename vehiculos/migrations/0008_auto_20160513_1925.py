# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0007_auto_20160513_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculomodel',
            name='clase',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
