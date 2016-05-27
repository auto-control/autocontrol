# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mecanicomodel',
            name='documento',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='mecanicomodel',
            name='fnaci',
            field=models.DateField(null=True, blank=True),
        ),
    ]
