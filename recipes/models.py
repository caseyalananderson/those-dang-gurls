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
    Class that holds all the recipe names
    """

    title = models.CharField(max_length=50)
    description = RichTextUploadingField(null=True)
    content = RichTextUploadingField(null=True)

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
    Images for the Recipe
    """
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_upload_path)
    cover_photo = models.BooleanField(default=False)
    recipe = models.ForeignKey(Recipe, null=True, blank=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name
