# -*- coding: utf-8 -*-
from django.test import SimpleTestCase
from models.line_sugested import LineSugested
from models.terminal import Terminal



class TestLineSugested(SimpleTestCase):



    def create_terminal(self):
        terminal = Terminal()
        terminal.description = "description"
        terminal.address = "address"
        terminal.save()
        return terminal

    def createsugested_line(self, description, justify, line_number):
            terminal = self.create_terminal()
            line_sugest = LineSugested()
            line_sugest.description = description
            line_sugest.justify = justify
            line_sugest.busline = line_number
            line_sugest.terminal = terminal
            line_sugest.save()
            return line_sugest

    def test_instance(self):
        self.createsugested_line("aeiou", "aeio")
        sugested_lines = LineSugested.all()
        self.assertEquals(1, len(sugested_lines))

    def test_filter_by_line_number(self):
        self.createsugested_line("aeioy", "awert")
        sugested_lines = LineSugested.filter_by_line_number("003")
        self.assertEquals(1, len(sugested_lines))
