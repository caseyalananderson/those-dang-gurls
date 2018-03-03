# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-03 18:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0017_auto_20180303_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('comment_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('approved_comment', models.BooleanField(default=False)),
                ('food_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='food.FoodEntry')),
            ],
        ),
    ]