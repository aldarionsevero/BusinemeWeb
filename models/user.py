# Class user
from django.contrib.auth.models import User
from django.db import models


class User(User):

    """docstring for User"""
    pontuation = models.IntegerField(default=0)
