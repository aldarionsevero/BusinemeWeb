# -*- coding: utf-8 -*-

from django.test import SimpleTestCase
from models.busline import Busline


class BuslineTest(SimpleTestCase):

    def setUp(self):
        self.busline = Busline()
