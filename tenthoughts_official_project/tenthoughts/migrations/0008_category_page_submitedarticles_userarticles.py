# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenthoughts', '0007_remove_group_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('views', models.IntegerField(default=0)),
                ('category', models.ForeignKey(to='tenthoughts.Category', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubmitedArticles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('last_name', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=128)),
                ('article_url', models.URLField()),
                ('article_title', models.CharField(max_length=128)),
                ('article2_url', models.URLField(null=True)),
                ('article2_title', models.CharField(null=True, max_length=128)),
                ('article3_url', models.URLField(null=True)),
                ('article3_title', models.CharField(null=True, max_length=128)),
                ('date_submitted', models.DateTimeField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserArticles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('client_name', models.CharField(max_length=128)),
                ('client_firstname', models.CharField(max_length=128)),
                ('client_email', models.EmailField(max_length=75)),
                ('title_1', models.CharField(max_length=128)),
                ('url_1', models.URLField()),
                ('recommender_1', models.CharField(max_length=128)),
                ('title_2', models.CharField(max_length=128)),
                ('url_2', models.URLField()),
                ('recommender_2', models.CharField(max_length=128)),
                ('title_3', models.CharField(max_length=128)),
                ('url_3', models.URLField()),
                ('recommender_3', models.CharField(max_length=128)),
                ('title_4', models.CharField(max_length=128)),
                ('url_4', models.URLField()),
                ('recommender_4', models.CharField(max_length=128)),
                ('title_5', models.CharField(max_length=128)),
                ('url_5', models.URLField()),
                ('recommender_5', models.CharField(max_length=128)),
                ('title_6', models.CharField(max_length=128)),
                ('url_6', models.URLField()),
                ('recommender_6', models.CharField(max_length=128)),
                ('title_7', models.CharField(max_length=128)),
                ('url_7', models.URLField()),
                ('recommender_7', models.CharField(max_length=128)),
                ('title_8', models.CharField(max_length=128)),
                ('url_8', models.URLField()),
                ('recommender_8', models.CharField(max_length=128)),
                ('title_9', models.CharField(max_length=128)),
                ('url_9', models.URLField()),
                ('recommender_9', models.CharField(max_length=128)),
                ('title_10', models.CharField(max_length=128)),
                ('url_10', models.URLField()),
                ('recommender_10', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
