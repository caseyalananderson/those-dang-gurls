# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Beauty, Image

# Register your models here.


class ImageInline(admin.TabularInline):
    model = Image


class BeautyAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    exclude = ('slug', 'author',)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


admin.site.register(Beauty, BeautyAdmin)
