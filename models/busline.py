# -*- coding: utf-8 -*-
""" docstring for package Busline """
from django.db import models
from api.busline import BuslineAPI
from exception.api import ApiException


class Busline(models.Model):

    """ docstring for Busline """

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
        api = BuslineAPI()
        try:
            objects = api.all()
        except ApiException:
            objects = cls.objects.all()
        return objects

    @classmethod
    def filter_by_line_number(cls, line_number):
        api = BuslineAPI()
        try:
            objects = api.filter_by_line(line_number)
        except ApiException:
            objects = cls.objects.filter(line_number__startswith=line_number)
        return objects

    @classmethod
    def filter_by_description(cls, description):
        api = BuslineAPI()
        try:
            objects = api.filter_by_description(description)
        except ApiException:
            objects = cls.objects.filter(description__startswith=description)

        return objects

    @classmethod
    def filter_by_multiple(cls, line_number, description,
                           terminal__description):
        """
        Perform an advanced search filtering the results by the line number,\
        description and terminal description entered by the user then returns\
        the results list.
        """

        api = BuslineAPI()
        try:
            objects = api.filter(
                line_number=line_number,
                description=description,
                terminal__description=terminal__description
            )
        except ApiException:
            objects = cls.objects.filter(
                description__startswith=description,
                line_number__startswith=line_number,
                # terminals__startswith=terminals #FIXME forekey
            )

        return objects
