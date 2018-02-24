from django.db import models

# Create your models here.
# from recipes.models import Recipe


class Video(models.Model):
    """
    Some of the Videos we have made

    """
    title = models.CharField(max_length=30)
    published_date = models.DateField(auto_now_add=True)
    youtube_link = models.URLField(null=False)
    text = models.TextField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
