# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import recipes.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20180224_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(null=True, upload_to=recipes.models.get_upload_path),
        ),
    ]
