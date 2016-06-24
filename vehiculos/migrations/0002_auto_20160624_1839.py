# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehiculomodel',
            old_name='tipo',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='vehiculomodel',
            old_name='clase',
            new_name='linea',
        ),
        migrations.AddField(
            model_name='vehiculomodel',
            name='modelo',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
