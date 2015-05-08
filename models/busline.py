# -*- coding: utf-8 -*-
from django.db import models
import api.Busline


class Busline(models.Model):

    """docstring for Busline"""

    line_number = models.CharField(max_length=5, unique=True)
    description = models.CharField(max_length=255)
    via = models.CharField(max_length=255)
    route_size = models.FloatField()  # unit: kilometers
    fee = models.FloatField()  # unit: BRL (R$)
    company = models.ForeignKey('Company', null=True)
    terminals = models.ManyToManyField('Terminal')

    def __unicode__(self):
        return self.line_number + "-" + self.description

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def filter_by_line_number(cls, line_number):
        try:
            objects = filter_by_line(line_number)
        except:
            objetcts = cls.objects.filter(line_number__startswith=line_number)
        return objects

    @classmethod
    def filter_by_via(cls, via):
        return cls.objects.filter(via__startswith=via)

   # @classmethod
    # def  filter_by_description(cls,description):
     #   try:
      #      objects=filter_by_line(description)
       # except:
        #    objetcts=cls.objects.filter(line_number__startswith=description)
        # return objects
