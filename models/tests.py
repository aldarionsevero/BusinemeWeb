# -*- coding: utf-8 -*-

"""
docstring

"""
from django.contrib.auth.models import User
from django.test import SimpleTestCase


class WebModelUser(SimpleTestCase):
    """ docstring """

    def test_model_instance(self):
        """ Docstring to model instance """

        user = User()
        self.assertIsNotNone(user)

    def test_validate_paramethers(self):
        user = User(first_name="JOSE", password="12345678*",
                                email="jose@tese", username="jose")
        user.save()
        self.assertEquals(user.first_name, "JOSE")
        self.assertEquals(user.password, "12345678*")
        self.assertEquals(user.email, "jose@tese")
        self.assertEquals(user.username, "jose")
