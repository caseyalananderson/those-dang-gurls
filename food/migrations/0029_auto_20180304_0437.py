# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-04 04:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0028_auto_20180304_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(default=None, unique=True),
        ),
        migrations.AlterField(
            model_name='foodpost',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
