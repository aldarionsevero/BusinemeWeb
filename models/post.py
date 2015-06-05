# -*- coding: utf-8 -*-
from django.db import models


class Post(models.Model):
    comment = models.CharField(max_length=255)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    traffic = models.IntegerField()
    capacity = models.IntegerField()
    busline = models.ManyToManyField('Busline')
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __unicode__(self):
        return self.comment
        # Don't know how exactly use this def.
        # if i'm wrong, please set right

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def filter_by_date(cls, date):
        return cls.objects.all(date__contains=date)

    @classmethod
    def filter_by_time(cls, time):
        return cls.objects.all(time__contains=time)
