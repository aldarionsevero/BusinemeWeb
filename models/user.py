# Class user
from django.contrib.auth.models import User as DjangoUser
from django.db import models


class User(DjangoUser):

    """docstring for User"""
    pontuation = models.IntegerField(default=0)

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def filter_by_username(cls, username):
        return cls.objects.filter(username=username)

    def validate_user_name(self):
        if self.filter_by_username(self.username) is None:
            return True
        else:
            return False
