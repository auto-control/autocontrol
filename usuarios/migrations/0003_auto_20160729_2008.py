# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20160729_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuariosmodel',
            name='cedula',
        ),
        migrations.RemoveField(
            model_name='usuariosmodel',
            name='celular',
        ),
    ]
