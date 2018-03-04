from django.db import models

# These two below are for auto-updating the youtube embed link
import re
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
# from recipes.models import Recipe
from food.models import FoodPost


class Video(models.Model):
    """
    Some of the Videos we have made

    """
    title = models.CharField(max_length=30)
    published_date = models.DateField(auto_now_add=True)
    youtube_link = models.URLField(null=False)
    youtube_embed_link = models.URLField(max_length=100, blank=True)
    description = models.TextField(null=True)
    related_foodentry = models.ForeignKey(FoodPost, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        # exclude = ['youtube_embed_link']


@receiver(post_save, sender=Video)
def handler_that_saves_a_mymodel_instance(sender, instance, created, **kwargs):
    # without this check the save() below causes infinite post_save signals
    if created:
        instance.youtube_embed_link = create_youtube_embed_link(instance.youtube_link)
        instance.save()


def create_youtube_embed_link(youtube_link):
    try:
        embed_str = youtube_link.split('watch?v=')[1]
        youtube_embed_link = 'http://www.youtube.com/embed/%s' % embed_str
        return youtube_embed_link
    except:
        return ''

