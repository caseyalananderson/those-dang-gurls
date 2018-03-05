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
    exclude = ('slug', 'author',)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class FoodPostAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    exclude = ('slug', 'author',)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(FoodPost, FoodPostAdmin)
