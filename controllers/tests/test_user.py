# -*- coding: utf-8 -*-

from django.test import SimpleTestCase, Client
from models.user import User

STATUS_OK = 200
STATUS_REDIRECT = 302


class UserControllerTest(SimpleTestCase):

    def setUp(self):
        self.client = Client()

    def create_user(self):
        self.user = User()
        self.user.username = 'test_username'
        self.user.password = 'test_password'
        self.user.name = 'test_name'
        self.user.email = 'test@email.tes'
        self.user.save()

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

    def new_password(self):
        data = {'password': '4321'}
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
        self.client.post('/cadastrar/usuario/', data)
        db_after = User.objects.all().count()
        self.assertTrue(db_after > db_before)

    def test_loged_user(self):
        self.create_user()
        self.client.login(username='test_username', password='test_password')
        response = self.client.get('/login/')
        self.assertEquals(response.status_code, STATUS_OK)
        self.client.logout()
        self.user.delete()

    def test_logout_user(self):
        response = self.client.get('/login/?next=/sair/')
        self.assertEquals(response.status_code, STATUS_OK)

    def test_user_account(self):
        response = self.client.get('/perfil/')
        self.assertEquals(response.status_code, STATUS_REDIRECT)

    def test_change_password_page(self):
        response = self.client.get('/alterarcao_senha/ ')
        self.assertEquals(response.status_code, STATUS_REDIRECT)

    def test_change_password(self):
        response = self.client.get(
            '/alterar_senha/', self.new_password())
        self.assertEquals(response.status_code, STATUS_REDIRECT)

    def test_change_userdate(self):
        data = self.register_post_data()
        response = self.client.post('/alterar_dados/', data)
        self.assertEquals(response.status_code, STATUS_REDIRECT)

    def test_deactivate_account_page(self):
        response = self.client.get('/desativacao_perfil/')
        self.assertEquals(response.status_code, STATUS_REDIRECT)

    def test_buscar_linha_page(self):
        data = {'busline': '205'}
        response = self.client.post('/buscar_linha/', data)
        self.assertEquals(response.status_code, STATUS_OK)
