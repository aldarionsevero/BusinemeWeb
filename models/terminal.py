# -*- coding: utf-8 -*-

from django.db import models


class Terminal(models.Model):

    """Terminal Models"""
    description = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        """Returns its own description (usually the terminal name)"""
        return self.description

    @classmethod
    def all(cls):
        r"""
        Returns all terminals.
        """
        return cls.objects.all()

    @classmethod
    def filter_by_address(cls, address):
        r"""
        Returns all companies containing the specified address.
        """
        return cls.objects.filter(address__contains=address)
