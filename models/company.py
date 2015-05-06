# -*- coding: utf-8 -*-
from django.db import models


class Company(models.Model):

    """docstring for Company"""
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def filter_by_name(cls, name):
        return cls.objects.filter(name__contains=name)
