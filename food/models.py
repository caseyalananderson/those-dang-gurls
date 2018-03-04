from django.db import models
import os
from django.conf import settings
import datetime
from comments.models import Comment
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import reverse


class FoodEntryManager(models.Manager):
    """
    Manage for the Comment section
    """
    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(FoodEntryManager, self).filter(content_type=content_type, object_id=obj_id)
        return qs


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

    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    title = models.CharField(max_length=50)
    cover_photo = models.ImageField(upload_to=get_upload_path, null=True)

    servings = models.CharField(max_length=5)
    prep_time = models.CharField(max_length=20)
    cook_time = models.CharField(max_length=20)
    total_time = models.CharField(max_length=20)

    directions = RichTextUploadingField(null=True)
    notes = RichTextUploadingField(null=True)

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
    Class that holds all the entries
    """

    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

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

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @ property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

    def get_absolute_url(self):
        return reverse("food_post", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return self.recipe.title

    def __unicode__(self):
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

