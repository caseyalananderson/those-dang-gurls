# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-04 03:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0022_auto_20180303_2028'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FoodEntry',
            new_name='FoodPost',
        ),
    ]
