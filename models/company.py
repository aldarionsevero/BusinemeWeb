# -*- coding: utf-8 -*-
from django.db import models


class Company(models.Model):

    """Company Model"""
    name = models.CharField(max_length=255)

    def __unicode__(self):
        """Returns its own name"""
        return self.name

    @classmethod
    def all(cls):
        r"""
        Returns all companies.
        """
        return cls.objects.all()

    @classmethod
    def filter_by_name(cls, name):
        r"""
        Returns all companies containing the specified name.
        """
        return cls.objects.filter(name__contains=name)
