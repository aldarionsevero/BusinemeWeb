# -*- coding: utf-8 -*-

from django.test import SimpleTestCase, Client
from models.user import User

STATUS_OK = 200
STATUS_REDIRECT = 302


class UserControllerTest(SimpleTestCase):

    def setUp(self):
        self.client = Client()
        self.user = User()
        self.user.username = 'test_user'
        self.user.password = '1234'

    def register_post_data(self):
        data = {'name': 'test_user',
                'email': 'test@email.com',
                'username': 'test_user',
                'password': '1234'}
        return data

    def login_post_data(self):
        data = {'username': 'test_user',
                'password': '1234'}
        return data

    def test_register_user_page(self):
        response = self.client.get('/cadastro/')
        self.assertEquals(response.status_code, STATUS_OK)

    def test_register_user_success_status_code(self):
        data = self.register_post_data()
        response = self.client.post('/cadastrar/usuario/', data)
        self.assertEquals(response.status_code, STATUS_OK)

    def test_register_user_success_db(self):
        data = self.register_post_data()
        db_before = User.objects.all().count()
        response = self.client.post('/cadastrar/usuario/', data)
        db_after = User.objects.all().count()
        self.assertTrue(db_after > db_before)
