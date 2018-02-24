# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('vegan', models.BooleanField(default=False)),
                ('healthy', models.CharField(max_length=25, choices=[(b'HEALTHY', b'Healthy'), (b'CLOSE', b'You can spin it that way'), (b'MAYBE', b'Its complicated'), (b'NOT REALLY', b'Its really delicious!')])),
            ],
        ),
        migrations.DeleteModel(
            name='Ingredients',
        ),
        migrations.DeleteModel(
            name='Recipes',
        ),
    ]
