# -*- coding: utf-8 -*-
from django.db import models


class Company(models.Model):

    """docstring for Company"""
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
