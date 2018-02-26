# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import recipes.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20180226_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='img1',
            field=models.ImageField(null=True, upload_to=recipes.models.get_upload_path, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='img10',
            field=models.ImageField(null=True, upload_to=recipes.models.get_upload_path, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='img11',
            field=models.ImageField(null=True, upload_to=recipes.models.get_upload_path, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='img12',
            field=models.ImageField(null=True, upload_to=recipes.models.get_upload_path, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='img13',
            field=models.ImageField(null=True, upload_to=recipes.models.get_upload_path, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='img14',
            field=models.ImageField(null=True, upload_to=recipes.models.get_upload_path, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='img15',
            field=models.ImageField(null=True, upload_to=recipes.models.get_upload_path, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='img16',
            field=models.ImageField(null=True, upload_to=recipes.models.get_upload_path, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='img17',
            field=models.ImageField(null=True, upload_to=recipes.models.get_upload_path, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='img18',
            field=models.ImageField(null=True, upload_to=recipes.models.get_upload_path, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='img19',
            field=models.ImageField(null=True, upload_to=recipes.models.get_upload_path, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='img2',
            field=models.ImageField(null=True, upload_to=recipes.models.get_upload_path, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='img20',
            field=models.ImageField(null=True, upload_to=recipes.models.get_upload_path, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='img3',
            field=models.ImageField(null=True, upload_to=recipes.models.get_upload_path, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='img4',
            field=models.ImageField(null=True, upload_to=recipes.models.get_upload_path, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='img5',
            field=models.ImageField(null=True, upload_to=recipes.models.get_upload_path, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='img6',
            field=models.ImageField(null=True, upload_to=recipes.models.get_upload_path, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='img7',
            field=models.ImageField(null=True, upload_to=recipes.models.get_upload_path, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='img8',
            field=models.ImageField(null=True, upload_to=recipes.models.get_upload_path, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='img9',
            field=models.ImageField(null=True, upload_to=recipes.models.get_upload_path, blank=True),
        ),
    ]
