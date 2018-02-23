from django.db import models


class Recipes(models.Model):
    """
    Class that holds all the recipe names
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    """
    Class that holds the ingredients
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
