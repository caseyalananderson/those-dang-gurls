# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_auto_20180227_0241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='main_photo',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='health',
        ),
        migrations.AddField(
            model_name='recipe',
            name='gluten_free',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recipe',
            name='healthy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recipe',
            name='vegetarian',
            field=models.BooleanField(default=False),
        ),
    ]
