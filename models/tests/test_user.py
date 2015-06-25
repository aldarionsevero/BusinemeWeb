# -*- coding: utf-8 -*-

from django.test import SimpleTestCase
from models.user import User


class TestUser(SimpleTestCase):

    def create_user(self):
        User.objects.all().delete()
        user = User()
        user.username = "test_test"
        user.set_password('1234')
        user.name = 'test_name'
        user.email = 'test@email.tes'
        user.save()

    def test_unicode(self):
        User.objects.all().delete()
        user = User()
        user.username = "test_test"
        user.set_password('1234')
        user.name = 'test_name'
        user.email = 'test@email.tes'
        self.assertEquals(user.__unicode__(), "test_test")
