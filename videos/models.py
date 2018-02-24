from django.db import models

# Create your models here.
from recipes.models import Recipe
from blog.models import BlogPost


class Video(models.Model):
    """
    Some of the Videos we have made

    """
    title = models.CharField(max_length=30)
    published_date = models.DateField(auto_now_add=True)
    youtube_link = models.URLField(null=False)
    description = models.TextField(null=True)
    related_blog = models.ForeignKey(BlogPost, null=True)
    related_recipe = models.ForeignKey(Recipe, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
