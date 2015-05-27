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

    def test_register_user_duplicate_email(self):
        data1 = {'name': 'test_user1',
                 'email': 'same@email.com',  # same email
                 'username': 'test_user1',
                 'password': '1234'}
        data2 = {'name': 'test_user2',
                 'email': 'same@email.com',  # same email
                 'username': 'test_user2',
                 'password': '1234'}
        response1 = self.client.post('/cadastrar/usuario/', data1, follow=True)
        response2 = self.client.post('/cadastrar/usuario/', data2, follow=True)

        self.assertEquals(
            response1.redirect_chain, [('http://testserver/login/', 302)])
        self.assertEquals(
            response2.redirect_chain, [])
        self.assertEquals(response1.status_code, STATUS_OK)
        self.assertEquals(response2.status_code, STATUS_OK)

    def test_register_user_invalid_email(self):
        data = {'name': 'test_user2',
                'email': 'testemail.com',
                'username': 'test_user2',
                'password': '1234'}
        response = self.client.post('/cadastrar/usuario/', data, follow=True)
        self.assertEquals(response.redirect_chain, [])
        self.assertEquals(response.status_code, STATUS_OK)

    def test_register_user_invalid_username(self):
        data1 = {'name': 'test_user1',  # same name
                 'email': 'test1@email.com',
                 'username': 'test_user_same',
                 'password': '1234'}
        data2 = {'name': 'test_user2',  # same name
                 'email': 'test2@email.com',
                 'username': 'test_user_same',
                 'password': '1234'}
        response1 = self.client.post('/cadastrar/usuario/', data1, follow=True)
        response2 = self.client.post('/cadastrar/usuario/', data2, follow=True)

        self.assertEquals(
            response1.redirect_chain, [('http://testserver/login/', 302)])
        self.assertEquals(
            response2.redirect_chain, [])
        self.assertEquals(response1.status_code, STATUS_OK)
        self.assertEquals(response2.status_code, STATUS_OK)

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

    # FIX-ME
    def test_register_user_page_feed(self):
        self.create_user()
        self.client.login(
            username='test_username', password='test_password')
        response = self.client.get('/')
        self.assertEquals(response.status_code, STATUS_OK)
        self.client.logout()
        self.user.delete()
