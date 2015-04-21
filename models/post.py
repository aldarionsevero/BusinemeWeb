# -*- coding: utf-8 -*-
from django.db import models


class Post(models.model):
    comment = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    traffic = models.IntegerField()
    capacity = models.IntegerField()
    terminals = models.ManyToMany('Terminal')
    date = models.DateField.auto_now()
    time = models.TimeField.auto_now()

    def __unicode__(self):
        return self.comment
        # Don't know how exactly use this def.
        # if i'm wrong, please set right
