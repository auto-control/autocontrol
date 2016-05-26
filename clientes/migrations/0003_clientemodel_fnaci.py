# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20160420_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientemodel',
            name='fnaci',
            field=models.DateField(null=True, blank=True),
        ),
    ]
