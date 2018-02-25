# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_auto_20180225_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='youtube_embed_link',
            field=models.URLField(max_length=100, blank=True),
        ),
    ]
