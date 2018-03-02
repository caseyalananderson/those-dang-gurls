from django.db import models
import os
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField


def get_upload_path(instance, filename):
    """
    Gets path of
    :param instance:
    :param filename:
    :return:
    """
    no_space_title = str(instance.recipe.title.replace(' ', ''))
    return os.path.join("uploads", no_space_title, filename)


class Recipe(models.Model):
    """
    Recipe summary for the
    """

    TIMES_UNITS = (
        ('minutes', 'minutes'),
        ('hours', 'hours'),
    )

    name = models.CharField(max_length=50)
    servings = models.CharField(max_length=5)
    time_unit = models.CharField(choices=TIMES_UNITS, default='minutes', max_length=10)
    prep_time = models.CharField(max_length=3)
    cook_time = models.CharField(max_length=3)
    total_time = models.CharField(max_length=3)


class FoodEntry(models.Model):
    """
    Class that holds all the recipe names
    """

    title = models.CharField(max_length=50)
    summary = RichTextUploadingField(null=True)
    foodprep = RichTextUploadingField(null=True)
    content = RichTextUploadingField(null=True)

    recipe = models.ForeignKey(Recipe, null=True, blank=True, on_delete=models.CASCADE)

    breakfast = models.BooleanField(default=False)
    entree = models.BooleanField(default=False)
    snack = models.BooleanField(default=False)
    desert = models.BooleanField(default=False)
    savory = models.BooleanField(default=False)

    vegan = models.BooleanField(default=False)
    healthy = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Image(models.Model):
    """
    Images for the Food Entry
    """
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=get_upload_path)
    cover_photo = models.BooleanField(default=False)
    foodentry = models.ForeignKey(FoodEntry, null=True, blank=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name




