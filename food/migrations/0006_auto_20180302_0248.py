# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-02 02:48
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import food.models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_remove_image_cover_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='FullIngredientList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=10)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.FullIngredientList')),
            ],
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='recipe',
            name='cover_photo',
            field=models.ImageField(null=True, upload_to=food.models.get_upload_path),
        ),
        migrations.AddField(
            model_name='recipe',
            name='directions',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='notes',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
