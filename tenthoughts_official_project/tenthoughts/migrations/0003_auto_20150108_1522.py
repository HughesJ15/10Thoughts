# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenthoughts', '0002_auto_20150108_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprof',
            name='groups',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
    ]
