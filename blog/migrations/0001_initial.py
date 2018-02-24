# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('published_date', models.DateField(auto_now_add=True)),
                ('text', models.TextField(null=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
