# -*- coding: utf-8 -*-

from django.db import models


class Terminal(models.model):
    """docstring for Terminal"""
    description = models.CharField(max_length=255)
    adress = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        return self.description
