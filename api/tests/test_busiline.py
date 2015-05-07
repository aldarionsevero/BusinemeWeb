# -*- coding: utf-8 -*-
from api.busline import BuslineAPI
from api.models import *

from django.test import SimpleTestCase


class testBusilineAPI(SimpleTestCase):

    """docstring for testBusilineAPI"""

    def setUp(self):
        self.busline = BuslineAPI()

    def test_models(self):
        instance = busline.Busline()
        self.assertIsNotNone(instance)
        instance = terminal.Terminal()
        self.assertIsNotNone(instance)
        instance = company.Company()
        self.assertIsNotNone(instance)

    def test_all(self):
        self.assertIsNotNone(self.busline.all())
        pass
