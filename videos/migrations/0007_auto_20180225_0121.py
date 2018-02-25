# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_auto_20180225_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='related_blog',
            field=models.ForeignKey(blank=True, to='blog.BlogPost', null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='related_recipe',
            field=models.ForeignKey(blank=True, to='recipes.Recipe', null=True),
        ),
    ]
