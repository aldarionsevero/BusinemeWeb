# -*- coding: utf-8 -*-
from django.db import models


class Post(models.Model):
    comment = models.CharField(max_length=255)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    traffic = models.IntegerField()
    capacity = models.IntegerField()
    terminals = models.ManyToManyField('Terminal')
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __unicode__(self):
        return self.comment
        # Don't know how exactly use this def.
        # if i'm wrong, please set right
