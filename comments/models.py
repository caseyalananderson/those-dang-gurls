# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.admin import GenericForeignKey


class CommentManager(models.Manager):
    """
    Manage for the Comment section
    """
    def all(self):
        """
        Overrides all method to only show the First comments
        """
        qs = super(CommentManager, self).filter(parent=None)
        return qs

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type=content_type, object_id=obj_id).filter(parent=None)
        return qs


class Comment(models.Model):
    """
    Comments for the website, managed by CommentManager
    """
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    parent = models.ForeignKey('self', null=True, blank=True)

    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    objects = CommentManager()

    def children(self):  # Replies
        return Comment.objects.filter(parent=self)

    class Meta:
        ordering = ['-timestamp']

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True

    def __str__(self):
        return str('comment')
