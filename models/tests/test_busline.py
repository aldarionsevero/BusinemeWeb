# -*- coding: utf-8 -*-

from django.test import SimpleTestCase
from models.busline import Busline
from models.terminal import Terminal
from exception.api import ApiException
from api.busline import BuslineAPI


class BuslineTest(SimpleTestCase):

    def create_busline(self):
        busline = Busline()
        busline.line_number = "001"
        busline.description = "description"
        busline.via = "via"
        busline.route_size = 2.5
        busline.fee = 2.0
        terminal = Terminal(description="terminal")
        terminal.save()
        busline.save()
        busline.terminals.add(terminal)
        return busline

    def flush_buslines(self):
        Busline.objects.all().delete()

    def setUp(self):
        self.flush_buslines()
        self.api = BuslineAPI()

    def test_busline_instance(self):
        busline = Busline()
        self.assertIsNotNone(busline)

    def test_busline_unicode(self):
        busline = self.create_busline()
        self.assertEquals("001-description", busline.__unicode__())

    def test_busline_all(self):
        self.create_busline()
        buslines = Busline.all()
        self.assertEquals(1, len(buslines))

    def test_busline_all_empty(self):
        buslines = Busline.all()
        self.assertEquals(0, len(buslines))

    def test_busline_filter_line_number(self):
        self.create_busline()
        buslines = Busline.filter_by_line_number("001")
        self.assertEquals(1, len(buslines))

    def test_busline_filter_invalid_line_number(self):
        buslines = Busline.filter_by_line_number("003")
        self.assertEquals(0, len(buslines))

    def test_busline_by_description(self):
        self.create_busline()
        buslines = Busline.filter_by_description("description")
        self.assertEquals(1, len(buslines))

    def test_busline_filter_by_description_invalid_description(self):
        self.create_busline()
        buslines = Busline.filter_by_description("aeiou")
        self.assertEquals(0, len(buslines))

    def test_busline_filter_by_multiple(self):
        self.create_busline()
        buslines = Busline.filter_by_multiple(
            "001", "description", "terminal_description")
        self.assertEquals(1, len(buslines))

    def test_busline_filter_by_multiple_invalid_description(self):
        self.create_busline()
        buslines = Busline.filter_by_multiple(
            "001", "invalid", "terminal_description")
        self.assertEquals(0, len(buslines))

    def teste_busline_filter_by_multiple_invalid_line_number(self):
        self.create_busline()
        buslines = Busline.filter_by_multiple(
            "000", "description", "terminal_description")
        self.assertEquals(0, len(buslines))

    def test_busline_filter_by_multiple_invalid_both(self):
        self.create_busline()
        buslines = Busline.filter_by_multiple(
            "000", "invalid", "terminal_description")
        self.assertEquals(0, len(buslines))

    def test_all_exception(self):
        Busline.all()
        self.assertRaises(ApiException)

    def test_filter_by_line_number_exception(self):
        Busline.filter_by_line_number('001')
        self.assertRaises(ApiException)

    def test_filter_by_description_exception(self):
        Busline.filter_by_description('description')
        self.assertRaises(ApiException)

    def test_filter_by_multiple_exception(self):
        Busline.filter_by_multiple(
            '001', 'description', 'terminal_description')
        self.assertRaises(ApiException)
