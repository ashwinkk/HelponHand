# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpreq', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loccache',
            name='lat',
            field=models.FloatField(max_length=20),
        ),
        migrations.AlterField(
            model_name='loccache',
            name='lon',
            field=models.FloatField(max_length=20),
        ),
    ]
