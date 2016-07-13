# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='empresaModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nit', models.CharField(max_length=35)),
                ('nombre', models.CharField(max_length=35)),
                ('representanteLegal', models.CharField(max_length=35)),
                ('telefono', models.IntegerField(max_length=20, null=True, blank=True)),
                ('pbx', models.CharField(max_length=10, null=True, blank=True)),
                ('direccion', models.CharField(max_length=50, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('numeracionAutorizada', models.IntegerField(max_length=20)),
            ],
        ),
    ]
