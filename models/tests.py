# -*- coding: utf-8 -*-

"""
docstring

"""
import models
from django.test import SimpleTestCase


class WebModelUser(SimpleTestCase):
    """ docstring """

    def test_model_instance(self):
        """ Docstring to model instance """

        user = models.user.User()
        self.assertIsNotNone(user)

    # def test_validate_paramethers(self):
    #     user = models.user.User(nome="JOSE", password="12345678*",
    #                             email="jose@tese", userName="jose")
    #     user.save()
    #     self.asserEqual(user.name, "JOSE")
    #     self.asserEqual(user.password, "12345678*")
    #     self.asserEqual(user.email, "jose@tese")
    #     self.asserEqual(user.userName, "jose")
