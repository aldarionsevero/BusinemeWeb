# -*- coding: utf-8 -*-
from django.db import models


class Company(models.model):

    """docstring for Company"""
    namo = models.CharField(max_lenght=255)

    def __unicode__(self):
        return self.name
