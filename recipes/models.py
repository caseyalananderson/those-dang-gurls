from django.db import models
import os
from django.conf import settings


def get_upload_path(instance, filename):
    """
    Gets path of
    :param instance:
    :param filename:
    :return:
    """
    no_space_title = str(instance.recipe.title.replace(' ', ''))
    return os.path.join("photos", no_space_title, 'images', filename)


class Recipe(models.Model):
    """
    Class that holds all the recipe names
    """

    HEALTH_LEVEL = (
        ('HEALTHY', 'Healthy'),
        ('CLOSE', 'You can spin it that way'),
        ('MAYBE', 'Its complicated'),
        ('NOT REALLY', 'Its really delicious!'),
    )

    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    instructions = models.TextField(null=True)

    vegan = models.BooleanField(default=False)
    health = models.CharField(choices=HEALTH_LEVEL, max_length=25)

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
    main_photo = models.BooleanField(default=False)
    recipe = models.ForeignKey(Recipe, null=True, blank=True)

    def __unicode__(self):
        return self.name
