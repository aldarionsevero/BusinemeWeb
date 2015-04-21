# -*- coding: utf-8 -*-
from django.db import models


class Busline(models.model):
    """docstring for Busline"""

    line_number = models.Charfield(max_length=5, unique=True)
    description = models.Charfield(max_length=255)
    via = models.Charfield(max_length=255)
    route_size = models.FloatField()  # unit: kilometers
    fee = models.FloatField()  # unit: BRL (R$)
    company = models.ForeignKey('Company', null=True)
    terminals = models.ManyToManyField('Terminal')

    def __unicode__(self):
        return self.line_number + "-" + self.description
