# -*- coding: utf-8 -*-

from django.db import models


class Terminal(models.Model):

    """docstring for Terminal"""
    description = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        return self.description
