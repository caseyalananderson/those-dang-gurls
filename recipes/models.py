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

    # HEALTH_LEVEL = (
    #
    #    ('Healthy', 'Healthy'),
    #    ('Close to healthy', 'Close to healthy'),
    #    ('Healthier than most deserts', 'Healthier than most deserts'),
    #    ('Its really delicious!', 'Its really delicious!'),
    # )

    # health = models.CharField(choices=HEALTH_LEVEL, max_length=25)

    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    instructions = models.TextField(null=True)
    # main_photo = models.OneToOneField(Image)

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
