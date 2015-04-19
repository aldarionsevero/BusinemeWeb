# -*- coding: utf-8-*-
from django.db import models


class Review(models.model):
    date = models.ManyToMany('Post')
    time = models.ManyToMany('Post')
    comment = models.CharField(max_length=10)
    # Belive thats a text, but if it's a "likeButton", please rectify

    def __unicode__(self):
        return self.comment
        # Don't know how exactly use this def.
        # if i'm wrong, please set right
