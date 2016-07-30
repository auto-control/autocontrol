# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tipoUsuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='usuariosmodel',
            name='tipoUsuario',
            field=models.ForeignKey(blank=True, to='usuarios.tipoUsuario', null=True),
        ),
    ]
