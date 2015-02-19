# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenthoughts', '0003_auto_20150108_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprof',
            name='groups',
            field=models.CharField(max_length=128, default='bschool'),
            preserve_default=True,
        ),
    ]
