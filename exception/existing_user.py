# -*- coding: utf-8 -*-


class ExistingUser(Exception):

    """docstring for ExistingUser"""

    def __str__(self):
        return "Usuário já existente"
