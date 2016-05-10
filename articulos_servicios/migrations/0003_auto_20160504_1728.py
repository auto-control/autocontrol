# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos_servicios', '0002_serviciomodel_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviciomodel',
            name='grupo',
            field=models.ForeignKey(blank=True, to='articulos_servicios.grupoServicioModel', null=True),
        ),
    ]
