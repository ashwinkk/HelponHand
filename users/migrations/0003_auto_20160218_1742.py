# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160218_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='regid',
            field=models.CharField(max_length=250),
        ),
    ]
