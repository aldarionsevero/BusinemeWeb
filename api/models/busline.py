# -*- coding: utf-8 -*-


class Busline(object):

    """API model for busline"""

    def __init__(self):
        r"""
        Initialize the atributes for the model.
        """
        self.line_number = ""
        self.description = ""
        self.via = ""
        self.route_size = 0.0
        self.fee = 0.0
        self.company = None
        self.terminals = []
