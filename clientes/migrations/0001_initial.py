# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clienteModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=35)),
                ('apellido', models.CharField(max_length=35)),
                ('documento', models.CharField(max_length=20)),
                ('fnaci', models.DateField(null=True, blank=True)),
                ('telefono', models.CharField(max_length=20, null=True, blank=True)),
                ('celular', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
            ],
        ),
    ]
