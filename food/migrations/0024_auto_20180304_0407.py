# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-04 04:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0023_auto_20180304_0353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='name',
            new_name='title',
        ),
    ]
