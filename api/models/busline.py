# -*- coding: utf-8 -*-


class Busline(object):

    """docstring for Busline"""

    def __init__(self):
        self.line_number = ""
        self.description = ""
        self.via = ""
        self.route_size = 0.0
        self.fee = 0.0
        self.company = None
        self.terminals = []
