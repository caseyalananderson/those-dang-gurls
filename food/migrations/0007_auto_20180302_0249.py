# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-02 02:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_auto_20180302_0248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='ingredient',
            new_name='ingredient_name',
        ),
    ]
