# -*- coding: utf-8 -*-

""" docstring for package sugest_line """
from django.db import models
from terminal import Terminal


class LineSugested(models.Model):

    line_number = models.CharField(max_length=6)
    description = models.CharField(max_length=255)
    justify = models.CharField(max_length=255)
    via = models.CharField(max_length=255, null=True)
    terminal = models.ForeignKey(Terminal, null=True)

    def __unicode__(self):
        """Return data of sugested line."""
        return 'line_number: %s description: %s justify: %s' % \
            (self.busline,
             self.description,
             self.justify)

    @classmethod
    def filter_by_line_number(cls, line_number):
        return cls.objects.filter(line_number__contains=line_number)

    @classmethod
    def all(cls):
        """Return all sugested lines."""
        return cls.objects.all()
