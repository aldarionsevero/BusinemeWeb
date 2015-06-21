from django.test import SimpleTestCase, Client
from models.post import Post
from controllers import post_controller
from exception.api import ApiException
from models.user import User


STATUS_OK = 200
STATUS_REDIRECT = 302


class PostControllerTest (SimpleTestCase):

    def setUp(self):
        self.client = Client()

    def create_user(self, username):
        self.user = User()
        self.user.username = username
        self.user.set_password('test_password')
        self.user.name = 'test_name'
        self.user.email = 'test@email.tes'
        self.user.save()

    def post_data(self, codigo_latitude, codigo_longitude, review):
        data = {'capacity': '5',
                'traffic': '5',
                'description': 'comment',
                'codigo_latitude': '0',
                'codigo_longitude': '0',
                'line_number': '001',
                'review': review}
        return data

    def test_make_post_page(self):
        response = self.client.get(
            "/realizar_post/?line_number=001&busline_id=01")
        self.assertEquals(response.status_code, STATUS_OK)

    def test_make_post_page_with_user(self):
        self.create_user('username-post-0')
        self.client.login(username='username-post-0', password='test_password')
        response = self.client.get(
            "/realizar_post/?line_number=001&busline_id=01")
        self.assertEquals(response.status_code, STATUS_OK)
        self.client.logout()
        self.user.delete()

    def test_make_post_action_page_with_user(self):
        self.create_user('username-post-1')
        self.client.login(username='username-post-1', password='test_password')
        response = self.client.post(
            "/realizar_post/", self.post_data('0', '0', '0'))
        self.assertEquals(response.status_code, STATUS_OK)
        self.client.logout()
        self.user.delete()

    def test_make_post_action_page_no_review(self):
        self.create_user('username-post-1')
        self.client.login(username='username-post-1', password='test_password')
        response = self.client.post(
            "/realizar_post/", self.post_data('0', '0', ''))
        self.assertEquals(response.status_code, STATUS_OK)
        self.client.logout()
        self.user.delete()

    def test_make_post_action_page_no_geolocation(self):
        self.create_user('username-post-1')
        self.client.login(username='username-post-1', password='test_password')
        response = self.client.post(
            "/realizar_post/", self.post_data('', '', '0'))
        self.assertEquals(response.status_code, STATUS_OK)
        self.client.logout()
        self.user.delete()
