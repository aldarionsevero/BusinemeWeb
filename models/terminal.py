# -*- coding: utf-8 -*-

from django.db import models
from api.terminal import TerminalAPI
from exception.api import ApiException


class Terminal(models.Model):

    """Terminal Model."""

    description = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        """Return its own description (usually the terminal name)."""
        return self.description

    @classmethod
    def all(cls):
        """Returns all terminals."""
        api = TerminalAPI()
        try:
            objects = api.all()
        except ApiException:
            objects = cls.objects.all()
        return objects

    @classmethod
    def filter_by_address(cls, address):
        """Return all companies containing the specified address."""
        return cls.objects.filter(address__contains=address)
