# -*- coding: utf-8 -*-


class LineWithoutPostError(Exception):

    """Exception for line without post."""

    def __str__(self):
        return "Line without post"
