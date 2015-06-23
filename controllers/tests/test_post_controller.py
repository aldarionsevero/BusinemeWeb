from django.test import SimpleTestCase, Client
from models.post import Post
from controllers import post_controller
from exception.api import ApiException
import urllib2
from models.user import User
from models.busline import Busline
from models.terminal import Terminal

STATUS_OK = 200
STATUS_REDIRECT = 302


class PostControllerTest (SimpleTestCase):

    def setUp(self):
        self.client = Client()
        Terminal.objects.all().delete()
        Busline.objects.all().delete()
        User.objects.all().delete()

    def create_user(self, username):
        self.user = User()
        self.user.username = username
        self.user.set_password('test_password')
        self.user.name = 'test_name'
        self.user.email = 'test@email.tes'
        self.user.save()

    def create_busline(self):
        busline = Busline()
        busline.line_number = "001"
        busline.description = "description"
        busline.via = "via"
        busline.route_size = 2.5
        busline.fee = 2.0
        terminal = Terminal(description="terminal")
        terminal.save()
        busline.save()
        busline.terminals.add(terminal)
        return busline

    def post_data(self, codigo_latitude, codigo_longitude, review):
        data = {'capacity': '5',
                'traffic': '5',
                'description': 'comment',
                'codigo_latitude': '0',
                'codigo_longitude': '0',
                'line_number': '001',
                'review': review}
        return data

    def twitter_data(self):
        data_twitter = {'capacity': '5',
                        'traffic': '5',
                        'line_number': '205'
                        }
        return data_twitter

    def test_make_post_page(self):
        response = self.client.get(
            "/realizar_post/?line_number=001&busline_id=01")
        self.assertEquals(response.status_code, STATUS_OK)

    def test_make_post_twitter(self):
        try:
            urllib2.urlopen('http://whatismyip.org').read()
            tweet_data = self.twitter_data()
            tweet = self._post_twitter(
                tweet_data['line_number'], tweet_data['capacity'],
                tweet_data['traffic'])
            self.assertTrue(tweet)
        except Exception:
            self.assertRaises(Exception)

    def test_make_post_page_with_user(self):
        self.create_user('username-post-0')
        self.client.login(username='username-post-0', password='test_password')
        response = self.client.get(
            "/realizar_post/?line_number=001&busline_id=01")
        self.assertEquals(response.status_code, STATUS_OK)
        self.client.logout()
        self.user.delete()

    def test_make_post_action_with_user(self):
        self.create_user('username-post-1')
        self.client.login(username='username-post-1', password='test_password')
        response = self.client.post(
            "/realizar_post/", self.post_data('0', '0', '0'))
        self.assertEquals(response.status_code, STATUS_OK)
        self.client.logout()
        self.user.delete()

    def test_make_post_action_with_user_and_line(self):
        busline = self.create_busline()
        self.create_user('username-post-2')
        self.client.login(username='username-post-2', password='test_password')
        response = self.client.post(
            "/realizar_post/", self.post_data('0', '0', '0'))
        self.assertEquals(response.status_code, STATUS_OK)
        self.client.logout()
        self.user.delete()
        busline.delete()

    def test_make_post_action_page_no_review(self):
        self.create_user('username-post-3')
        self.client.login(username='username-post-3', password='test_password')
        response = self.client.post(
            "/realizar_post/", self.post_data('0', '0', ''))
        self.assertEquals(response.status_code, STATUS_OK)
        self.client.logout()
        self.user.delete()

    def test_make_post_action_page_no_geolocation(self):
        self.create_user('username-post-4')
        self.client.login(username='username-post-4', password='test_password')
        response = self.client.post(
            "/realizar_post/", self.post_data('', '', '0'))
        self.assertEquals(response.status_code, STATUS_OK)
        self.client.logout()
        self.user.delete()
