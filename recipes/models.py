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
    return os.path.join("photos", no_space_title, filename)


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
    vegan = models.BooleanField(default=False)
    health = models.CharField(choices=HEALTH_LEVEL, max_length=25)
    main_photo = models.ImageField(upload_to=get_upload_path, null=True)
    img1 = models.ImageField(upload_to=get_upload_path, null=True)
    img2 = models.ImageField(upload_to=get_upload_path, null=True)
    img3 = models.ImageField(upload_to=get_upload_path, null=True)
    img4 = models.ImageField(upload_to=get_upload_path, null=True)
    img5 = models.ImageField(upload_to=get_upload_path, null=True)
    img6 = models.ImageField(upload_to=get_upload_path, null=True)
    img7 = models.ImageField(upload_to=get_upload_path, null=True)
    img8 = models.ImageField(upload_to=get_upload_path, null=True)
    img9 = models.ImageField(upload_to=get_upload_path, null=True)
    img10 = models.ImageField(upload_to=get_upload_path, null=True)
    img11 = models.ImageField(upload_to=get_upload_path, null=True)
    img12 = models.ImageField(upload_to=get_upload_path, null=True)
    img13 = models.ImageField(upload_to=get_upload_path, null=True)
    img14 = models.ImageField(upload_to=get_upload_path, null=True)
    img15 = models.ImageField(upload_to=get_upload_path, null=True)
    img16 = models.ImageField(upload_to=get_upload_path, null=True)
    img17 = models.ImageField(upload_to=get_upload_path, null=True)
    img18 = models.ImageField(upload_to=get_upload_path, null=True)
    img19 = models.ImageField(upload_to=get_upload_path, null=True)
    img20 = models.ImageField(upload_to=get_upload_path, null=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
