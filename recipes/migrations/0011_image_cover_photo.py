# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_auto_20180227_0319'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='cover_photo',
            field=models.BooleanField(default=False),
        ),
    ]
