# -*- coding: utf-8 -*-


class ExistingUser(Exception):

    """Exception for coflictiong usernames errors"""

    def __str__(self):
        return "Usuário já existente"
