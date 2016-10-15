# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=100)),
                ('phonenum', models.CharField(max_length=15, serialize=False, primary_key=True)),
                ('regid', models.CharField(max_length=250)),
            ],
        ),
    ]
