# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-02 02:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20180302_0218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='foodentry',
        ),
        migrations.AddField(
            model_name='foodentry',
            name='recipe',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='food.Recipe'),
        ),
    ]
