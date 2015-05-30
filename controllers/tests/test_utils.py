# -*- coding: utf-8 -*-

from django.test import SimpleTestCase, Client, RequestFactory
from models.user import User
from django.http import HttpRequest
from controllers.utils import error_message, response_htmlvars


class TestUtils(SimpleTestCase):

    def setUp(self):
        self.request = HttpRequest()
        self.data = {"name": "user_test", "email": "email@test.com",
                     "username": "usermane_test", "password": "1234"}
        self.STATUS_OK = 200
        self.STATUS_REDIRECT = 302
        self.factory = RequestFactory()

    def test_error_message_status_code(self):
        error = "errortest"
        response = error_message(
            error, error, error, "register.html", self.request)
        self.assertEquals(response.status_code, self.STATUS_OK)
# response.context[-1]
