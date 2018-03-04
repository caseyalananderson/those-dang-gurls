from django.db import models
import os
from comments.models import Comment
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import reverse
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.utils import timezone

from django.utils.text import slugify


class PublishedQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)

    def breakfast(self):
        return self.filter(breakfast=True)

    def entree(self):
        return self.filter(entree=True)

    def snack(self):
        return self.filter(snack=True)

    def dessert(self):
        return self.filter(dessert=True)

    def foodprep(self):
        return self.filter(foodprep=True)

    def beverage(self):
        return self.filter(beverage=True)

    def vegan(self):
        return self.filter(vegan=True)

    def vegetarian(self):
        return self.filter(vegetarian=True)

    def glutenfree(self):
        return self.filter(glutenfree=True)


class FoodPostManager(models.Manager):
    """
    Manage for the Comment section
    """
    def get_published_qs(self):
        return PublishedQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_published_qs().published()

    def breakfast(self):
        return self.get_published_qs().published().breakfast()

    def entree(self):
        return self.get_published_qs().published().entree()

    def snack(self):
        return self.get_published_qs().published().snack()

    def dessert(self):
        return self.get_published_qs().published().dessert()

    def foodprep(self):
        return self.get_published_qs().published().foodprep()

    def beverage(self):
        return self.get_published_qs().published().beverage()

    def vegan(self):
        return self.get_published_qs().published().vegan()

    def vegetarian(self):
        return self.get_published_qs().published().vegetarian()

    def glutenfree(self):
        return self.get_published_qs().published().glutenfree()

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(FoodPostManager, self).filter(content_type=content_type, object_id=obj_id)
        return qs


class RecipeManager(models.Manager):
    """
    Manager for the Recipes
    """

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(RecipeManager, self).filter(content_type=content_type, object_id=obj_id)
        return qs


def get_upload_path(instance, filename):
    """
    Gets path of file to upload
    :param instance:
    :param filename:
    :return:
    """
    no_space_title = str(instance.title.replace(' ', ''))
    return os.path.join("uploads", no_space_title, filename)


def get_image_upload_path(instance, filename):
    """
    Gets path of file to upload
    :param instance:
    :param filename:
    :return:
    """
    no_space_title = str(instance.foodpost.title.replace(' ', ''))
    return os.path.join("uploads", no_space_title, filename)


class Recipe(models.Model):
    """
    Recipe summary for the
    """

    slug = models.SlugField(unique=True, null=False, default=None)
    title = models.CharField(max_length=50, default=None)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    cover_photo = models.ImageField(upload_to=get_upload_path, null=True)

    servings = models.CharField(max_length=5)
    prep_time = models.CharField(max_length=20)
    cook_time = models.CharField(max_length=20)
    total_time = models.CharField(max_length=20)

    directions = RichTextUploadingField(null=True)
    notes = RichTextUploadingField(null=True)

    objects = RecipeManager()

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


class FoodPost(models.Model):
    """
    Class that holds all the entries
    """

    # Get the related recipe of the Food Post
    title = models.CharField(max_length=50)
    recipe = models.OneToOneField(Recipe, null=True, blank=True, on_delete=models.CASCADE)
    cover_photo = models.ImageField(upload_to=get_upload_path, null=True)

    slug = models.SlugField(unique=True, null=False, default=None)

    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    objects = FoodPostManager()

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
        return reverse("foodpost_detail", kwargs={"pk": self.pk})

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
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=get_image_upload_path)
    foodpost = models.ForeignKey(FoodPost, null=True, blank=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title


def create_foodpost_slug(instance, new_slug=None):
    """
    Creates a slug for the Food Post
    :param instance: recipe instance
    :param new_slug: new slug
    :return:
    """
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = FoodPost.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_foodpost_slug(instance, new_slug=new_slug)
    return slug


def create_recipe_slug(instance, new_slug=None):
    """
    Creates a slug for the recipe
    :param instance: recipe instance
    :param new_slug: new slug
    :return:
    """
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Recipe.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_recipe_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_post_receiver, sender=FoodPost)
pre_save.connect(pre_save_post_receiver, sender=Recipe)



