# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipe_photo'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('published_date', models.DateField(auto_now_add=True)),
                ('youtube_link', models.URLField()),
                ('description', models.TextField(null=True)),
                ('related_blog', models.ForeignKey(to='blog.BlogPost', null=True)),
                ('related_recipe', models.ForeignKey(to='recipes.Recipe', null=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
