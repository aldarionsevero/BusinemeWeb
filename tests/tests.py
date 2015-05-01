# -*- coding: utf-8 -*-

"""
docstring

"""

from django.test import SimpleTestCase
import controllers.user


class TesteWebControle(SimpleTestCase):
    """ docstring """

    myuser = controllers.user.User()

    def test_controle_user_instance(self):
        """ Docstring to model instance """
