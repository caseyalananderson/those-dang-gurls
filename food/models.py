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
    no_space_title = str(instance.title.replace(' ', ''))
    return os.path.join("uploads", no_space_title, filename)


def get_image_upload_path(instance, filename):
    """
    Gets path of
    :param instance:
    :param filename:
    :return:
    """
    no_space_title = str(instance.name.replace(' ', ''))
    return os.path.join("uploads", no_space_title, filename)


class Recipe(models.Model):
    """
    Recipe summary for the
    """

    TIMES_UNITS = (
        ('minutes', 'minutes'),
        ('hours', 'hours'),
    )

    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    title = models.CharField(max_length=50)
    cover_photo = models.ImageField(upload_to=get_upload_path, null=True)

    servings = models.CharField(max_length=5)
    time_unit = models.CharField(choices=TIMES_UNITS, default='minutes', max_length=10)
    prep_time = models.CharField(max_length=3)
    cook_time = models.CharField(max_length=3)

    directions = RichTextUploadingField(null=True)
    notes = RichTextUploadingField(null=True)

    total_time = models.CharField(max_length=3)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    """
    Ingredient
    """

    ingredient_name = models.CharField(max_length=40, blank=False, null=False)
    quantity = models.CharField(max_length=20, blank=False, null=False)
    recipe = models.ForeignKey(Recipe, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient_name


class FoodEntry(models.Model):
    """
    Class that holds all the recipe names
    """

    # Recipe
    recipe = models.OneToOneField(Recipe, null=True, blank=True, on_delete=models.CASCADE)

    # title = models.CharField(max_length=50)
    summary = RichTextUploadingField(null=True)
    foodprep = RichTextUploadingField(null=True)
    content = RichTextUploadingField(null=True)

    breakfast = models.BooleanField(default=False)
    entree = models.BooleanField(default=False)
    snack = models.BooleanField(default=False)
    desert = models.BooleanField(default=False)
    savory = models.BooleanField(default=False)

    vegan = models.BooleanField(default=False)
    healthy = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)

    published = models.BooleanField(default=False)

    def __str__(self):
        return self.recipe.title


class Image(models.Model):
    """
    Images for the Food Entry
    """
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=get_image_upload_path)
    foodentry = models.ForeignKey(FoodEntry, null=True, blank=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

