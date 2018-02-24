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
    no_space_title = str(instance.title).replace(' ', '')
    return os.path.join("photos",
                        no_space_title, filename)


class Recipe(models.Model):

    HEALTH_LEVEL = (
        ('HEALTHY', 'Healthy'),
        ('CLOSE', 'You can spin it that way'),
        ('MAYBE', 'Its complicated'),
        ('NOT REALLY', 'Its really delicious!'),
    )

    """
    Class that holds all the recipe names
    """
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    vegan = models.BooleanField(default=False)
    health = models.CharField(choices=HEALTH_LEVEL, max_length=25)
    photo = models.ImageField(upload_to=get_upload_path, null=True)

    def __str__(self):
        return self.title
