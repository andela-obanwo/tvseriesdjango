# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-22 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('o2tvseries', '0005_o2tvseries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='episode',
            unique_together=set([('show', 'season', 'episode_title')]),
        ),
        migrations.AlterUniqueTogether(
            name='season',
            unique_together=set([('show', 'season_no', 'title')]),
        ),
    ]
