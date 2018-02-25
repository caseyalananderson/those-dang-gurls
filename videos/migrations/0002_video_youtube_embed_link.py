# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='youtube_embed_link',
            field=models.URLField(null=True),
        ),
    ]
