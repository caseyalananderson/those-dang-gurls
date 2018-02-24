from django.db import models


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

    def __str__(self):
        return self.title
