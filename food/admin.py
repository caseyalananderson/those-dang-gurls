from django.contrib import admin
from .models import FoodPost, Recipe, Image, Ingredient


class ImageInline(admin.TabularInline):
    model = Image


class IngredientInline(admin.TabularInline):
    model = Ingredient


class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        IngredientInline,
    ]
    exclude = ('slug',)


class FoodPostAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    exclude = ('slug',)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(FoodPost, FoodPostAdmin)
