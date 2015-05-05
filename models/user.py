# Class user
from django.contrib.auth.models import User
from django.db import models


class User(User):

    """docstring for User"""
    pontuation = models.IntegerField(default=0)

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def filter_by_username(cls, name):
        return cls.objects.filter(username__startswith=name)
