# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.admin import GenericForeignKey


class CommentManager(models.Manager):
    """
    Manage for the Comment section
    """
    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type=content_type, object_id=obj_id)
        return qs


class Comment(models.Model):
    """
    Comments for the website, managed by CommentManager
    """
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    objects = CommentManager()

    parent = models.ForeignKey('self', null=True, blank=True)

    def children(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent:
            return True
        return False

    def __str__(self):
        return self.content