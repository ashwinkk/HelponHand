# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocCache',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phonenum', models.CharField(max_length=15)),
                ('lat', models.CharField(max_length=20)),
                ('lon', models.CharField(max_length=20)),
            ],
        ),
    ]
