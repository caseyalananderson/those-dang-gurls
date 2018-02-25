# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_auto_20180225_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='related_blog',
            field=models.ForeignKey(to='blog.BlogPost', blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='related_recipe',
            field=models.ForeignKey(to='recipes.Recipe', blank=True),
        ),
    ]
