# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0005_auto_20160420_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarcaModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marca', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='vehiculomodel',
            name='marca',
            field=models.ForeignKey(blank=True, to='vehiculos.MarcaModel', null=True),
        ),
    ]
