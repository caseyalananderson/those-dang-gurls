# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_video_youtube_embed_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='youtube_embed_link',
            field=models.URLField(default=b''),
        ),
    ]
