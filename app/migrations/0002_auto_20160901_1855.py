# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresamodel',
            name='numeracionAutorizada',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='empresamodel',
            name='telefono',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
