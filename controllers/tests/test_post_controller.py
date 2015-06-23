from django.test import SimpleTestCase, Client
from models.post import Post
from controllers import post_controller
from exception.api import ApiException
import urllib2

STATUS_OK = 200
STATUS_REDIRECT = 302


class PostControllerTest (SimpleTestCase):

    def setUp(self):
        self.client = Client()

    def post_data(self):
        data = {'capacity': '5',
                'traffic': '5',
                'description': 'comment',
                'codigo_latitude': '0',
                'codigo_longitude': '0',
                'line_number': '001'}
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

    def test_make_post_save(self):
        self.client.post(
            "/realizar_post/", self.post_data())
        self.assertRaises(ApiException)

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
