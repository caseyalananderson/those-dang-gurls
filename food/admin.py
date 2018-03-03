from django.contrib import admin
from .models import FoodEntry, Recipe, Image, Ingredient, Comment
from django.db import models


class ImageInline(admin.TabularInline):
    model = Image


class IngredientInline(admin.TabularInline):
    model = Ingredient


class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        IngredientInline,
    ]


# increase size
class FoodEntryAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(FoodEntry, FoodEntryAdmin)
admin.site.register(Comment)
