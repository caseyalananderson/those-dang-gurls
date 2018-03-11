from django.db import models
import os
from comments.models import Comment
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import reverse
from utils.utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.utils.text import slugify
from django.contrib.auth.models import User


class FitnessPostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)


class FitnessPostManager(models.Manager):
    """
    Manage for the Comment section
    """
    def get_fitnesspost_qs(self):
        return FitnessPostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_fitnesspost_qs().published()

    """
    Manager for the Recipes
    """

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(FitnessPostManager, self).filter(content_type=content_type, object_id=obj_id)
        return qs


def get_upload_path(instance, filename):
    """
    Gets path of file to upload
    :param instance:
    :param filename:
    :return:
    """
    upload_directory = str(instance.title.replace(' ', ''))
    upload_filename = filename
    return os.path.join("uploads/fitness", upload_directory, upload_filename)


def get_image_upload_path(instance, filename):
    """
    Gets path of file to upload
    :param instance:
    :param filename:
    :return:
    """
    base, extension = os.path.splitext(filename)
    upload_directory = str(instance.foodpost.title.replace(' ', ''))
    upload_filename = str(instance.title) + str(extension)
    return os.path.join("uploads/fitness", upload_directory, upload_filename)


class FitnessPost(models.Model):
    """
    Class that holds all the entries
    """

    # Hidden Fields
    author = models.ForeignKey(User, default=1)
    slug = models.SlugField(unique=True, null=False, default=None)

    # This is a boolean for now to show if you want it published
    published = models.BooleanField(default=False)

    # Dates
    publish_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    # Get the related recipe of the Food Post
    title = models.CharField(max_length=50)
    cover_photo = models.ImageField(upload_to=get_upload_path, blank=True, null=True)

    summary = RichTextUploadingField(blank=True, null=True)
    content = RichTextUploadingField(blank=True, null=True)

    youtube_link = models.URLField(max_length=100, blank=True, null=True)
    youtube_embed_link = models.URLField(max_length=100, blank=True, null=True)

    post_type = models.CharField(max_length=20, null=True, blank=True)

    objects = FitnessPostManager()

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
        return reverse("fitnesspost_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Image(models.Model):
    """
    Images for the Food Entry
    """
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=get_image_upload_path)
    fitnesspost = models.ForeignKey(FitnessPost, null=True, blank=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title


@receiver(post_save, sender=FitnessPost)
def handler_that_saves_a_mymodel_instance(sender, instance, created, **kwargs):
    # without this check the save() below causes infinite post_save signals
    if instance.post_type is None:
        instance.post_type = "fitness"
        instance.save()
    if instance.youtube_link and instance.youtube_embed_link is None:
        instance.youtube_embed_link = create_youtube_embed_link(instance.youtube_link)
        instance.save()


def create_youtube_embed_link(youtube_link):
    try:
        embed_str = youtube_link.split('watch?v=')[1]
        youtube_embed_link = 'http://www.youtube.com/embed/%s' % embed_str
        return youtube_embed_link
    except:
        return ''


def create_fitness_slug(instance, new_slug=None):
    """
    Creates a slug for the recipe
    :param instance: recipe instance
    :param new_slug: new slug
    :return:
    """
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = FitnessPost.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_fitness_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_post_receiver, sender=FitnessPost)
