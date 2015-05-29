# -*- coding: utf-8 -*-

from django.test import SimpleTestCase
from models.busline import Busline
from api.busline import BuslineAPI
from exception.api import ApiException


class BuslineTest(SimpleTestCase):

    def setUp(self):
        self.busline = Busline()
        self.api = BuslineAPI()

    def test_all_exception(self):
        objects = self.busline.all()
        self.assertRaises(ApiException)
        # self.assertEquals(objects, Busline.objects.all())

    # FIX ME
    # needs mock
    # def test_all_try_api(self):
    # mock api
    #     objects = self.busline.all()
    #     self.assertEquals(objects, self.api.all())

    def test_filter_by_line_number_exception(self):
        objects = self.busline.filter_by_line_number(205)
        self.assertRaises(ApiException)
        # self.assertEquals(objects, Busline.objects.filter_by_line_number(205))

    # FIX ME
    # needs mock
    # def test_filter_by_line_number_try_api(self):
    # mock api
    #     objects = self.busline.filter_by_line_number(205)
    #     self.assertEquals(objects, self.api.filter_by_line_number(205))

    def test_filter_by_via_exception(self):
        objects = self.busline.filter_by_via('w3')
        self.assertRaises(ApiException)
        # self.assertEquals(objects, Busline.objects.filter_by_via('w3'))

    # FIX ME
    # needs mock
    # def test_filter_by_via_try_api(self):
    # mock api
    #     objects = self.busline.filter_by_via('w3')
    #     self.assertEquals(objects, self.api.filter_by_via('w3'))

    def test_filter_by_description_exception(self):
        objects = self.busline.filter_by_description('w3')
        self.assertRaises(ApiException)
        # self.assertEquals(objects, Busline.objects.filter_by_description('w3'))

    # FIX ME
    # needs mock
    # def test_filter_by_description_try_api(self):
    # mock api
    #     objects = self.busline.filter_by_description('w3')
    #     self.assertEquals(objects, self.api.filter_by_description('w3'))

    def test_filter_by_multiple_exception(self):
        objects = self.busline.filter_by_multiple(205, 'w3', 'rodo')
        self.assertRaises(ApiException)
        # self.assertEquals(objects, Busline.objects.filter_by_multiple(205,'w3','rodo'))

    # FIX ME
    # needs mock
    # def test_filter_by_multiple_try_api(self):
    # mock api
    #     objects = self.busline.filter_by_multiple(205,'w3','rodo')
    #     self.assertEquals(objects, self.api.filter_by_multiple(205,'w3','rodo'))
