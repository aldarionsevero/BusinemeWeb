# Class user
from django.contrib.auth.models import User as DjangoUser
from django.db import models
import re


class User(DjangoUser):

    """docstring for User"""
    pontuation = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.username)

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def filter_by_username(cls, username):
        return cls.objects.filter(username=username)

    @classmethod
    def filter_by_email(cls, email):
        return cls.objects.filter(email=email)

    def validate_user_name(self):
        if User.filter_by_username(self.username) is None:
            return True
        else:
            return False

    def validate_email(self):
        if len(self.email) > 6:
            if re.match(r'\w[\w\.-]*@\w[\w\.-]+\.\w+', self.email) is not None:
                return True
        return False

    def validate_unique_email(self):
        users = User.filter_by_email(self.email)
        if len(users) == 0:
            return True
        else:
            return False

    def validade_user_password(self, userpassword):
        if len(userpassword) == 0:
            return False
        else:
            return True
