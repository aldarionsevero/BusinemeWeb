# -*- coding: utf-8-*-
from django.db import models


class Review(models.Model):
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    review_type = models.BooleanField(default=False)
    # Belive thats a text, but if it's a "likeButton", please rectify

    def __unicode__(self):
        return self.comment

    @classmethod
    def filter_all(cls):
        return cls.object.all()
