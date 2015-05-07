# -*- coding: utf-8 -*-
from api.busline import BuslineAPI


from django.test import SimpleTestCase


class testBusilineAPI(SimpleTestCase):

    """docstring for testBusilineAPI"""

    def setUp(self):
        self.busline = BuslineAPI()

    def testnoob(self):
        self.assertIsNone(None)
