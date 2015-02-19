# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenthoughts', '0004_auto_20150108_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprof',
            name='followers',
            field=models.TextField(default='email'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprof',
            name='following',
            field=models.TextField(default='email'),
            preserve_default=True,
        ),
    ]
