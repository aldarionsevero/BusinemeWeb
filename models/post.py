# -*- coding: utf-8 -*-
from django.db import models
from busline import Busline
from user import User


class Post(models.Model):

    """Busline model."""

    comment = models.CharField(max_length=255)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    traffic = models.IntegerField()
    capacity = models.IntegerField()
    busline = models.ForeignKey(Busline)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        """Return comment of the post."""
        return 'id: %s date: %s %s = ' % (self.id, str(self.date), str(self.time))

    @classmethod
    def all(cls):
        """Return all posts."""
        return cls.objects.all()
