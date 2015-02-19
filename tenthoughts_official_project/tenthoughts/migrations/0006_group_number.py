# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenthoughts', '0005_auto_20150109_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
