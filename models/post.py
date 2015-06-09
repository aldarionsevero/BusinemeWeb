# -*- coding: utf-8 -*-
from django.db import models
from busline import Busline


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

    def __unicode__(self):
        """Return comment of the post."""
        return  'id: %s date: %s %s = ' % (self.id, str(self.date), str(self.time))
            
    @classmethod
    def all(cls):
        """Return all posts."""
        return cls.objects.all()

    @classmethod
    def filter_by_date(cls, date):
        """Return all posts containing the specified date."""
        return cls.objects.all(date__contains=date)

    @classmethod
    def filter_by_time(cls, time):
        """Return all posts containing the specified time."""
        return cls.objects.all(time__contains=time)
