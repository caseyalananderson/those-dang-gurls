from django.db import models

# Create your models here.


class BlogPost(models.Model):
    """

    """
    title = models.CharField(max_length=30)
    published_date = models.DateField(auto_now_add=True)
    text = models.TextField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
