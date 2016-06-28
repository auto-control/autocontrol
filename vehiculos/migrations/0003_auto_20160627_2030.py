# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0002_auto_20160624_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='tipoLineaModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_tipo', models.CharField(max_length=50)),
                ('marca', models.ForeignKey(blank=True, to='vehiculos.MarcaModel', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='vehiculomodel',
            name='marca',
        ),
        migrations.AlterField(
            model_name='vehiculomodel',
            name='linea',
            field=models.ForeignKey(blank=True, to='vehiculos.tipoLineaModel', null=True),
        ),
    ]
