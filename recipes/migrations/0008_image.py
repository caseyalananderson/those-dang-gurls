# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import recipes.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_recipe_instructions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=recipes.models.get_upload_path)),
                ('main_photo', models.BooleanField(default=False)),
                ('recipe', models.ForeignKey(blank=True, to='recipes.Recipe', null=True)),
            ],
        ),
    ]
