# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes_servicios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenserviciodetallemodel',
            name='fecha',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
