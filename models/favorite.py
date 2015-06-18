# -*- coding utf-8 -*-
from django.db import models
from busline import Busline
from user import User


class Favorite (models.Model):

    """Favorite model"""

    user = models.ForeignKey(User)
    busline = models.ForeignKey(Busline)

    def __unicode__(self):
        """return comments of the favorite"""
        return 'User: %s, Busline id: %s' % (str(self.user),
                                             str(self.busline_id))

    @classmethod
    def all(cls):
        """return all objects of Favorite"""
        return cls.objects.all()
