# -*- coding: utf-8 -*-


class ApiException(Exception):

    """Exception for API errors."""

    def __str__(self):
        return "API Connection Error"
