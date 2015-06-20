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
        return 'User: %s, busline_id: %s' % (str(self.user_id),
                                             str(self.busline_id))

    @classmethod
    def all(cls):
        """return all objects of Favorite"""
        return cls.objects.all()

    @classmethod
    def alredy_favorite(cls, user_id, busline_id):
        """return a list of favorites """
        return cls.objects.filter(user_id=user_id, busline_id=busline_id)
