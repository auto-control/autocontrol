# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20160729_2008'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientemodel',
            name='cuenta',
            field=models.ForeignKey(blank=True, to='usuarios.usuariosModel', null=True),
        ),
    ]
