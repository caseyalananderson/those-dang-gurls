from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import Recipe, Image


class ImageInline(admin.TabularInline):
    model = Image


# increase size
class RecipeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 40, 'cols': 80})},
    }
    inlines = [
        ImageInline,
    ]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Image)

