from django.test import SimpleTestCase, Client
from models.post import Post
from controllers.post_controller import post_twitter
from exception.api import ApiException
from models.user import User
from models.busline import Busline
from models.terminal import Terminal
from mock import Mock
from mock import patch

STATUS_OK = 200
STATUS_REDIRECT = 302


class PostControllerTest (SimpleTestCase):

    def setUp(self):
        self.client = Client()

    def create_user(self):
        User.objects.all().delete()
        self.user = User()
        self.user.id = 1
        self.user.username = 'test_user'
        self.user.set_password('test_password')
        self.user.name = 'test_name'
        self.user.email = 'test@email.tes'
        self.user.save()

    def create_busline(self):
        Busline.objects.all().delete()
        self.busline = Busline()
        self.busline.id = 1
        self.busline.line_number = "0.001"
        self.busline.description = "description"
        self.busline.via = "via"
        self.busline.route_size = 2.5
        self.busline.fee = 2.0
        self.busline.save()

        Terminal.objects.all().delete()
        terminal = Terminal(description="terminal")
        terminal.save()

        self.busline.terminals.add(terminal)

    def post_data(self, capacity, traffic, review, comment, line):
        data = {'capacity': '5',
                'traffic': '5',
                'description': 'comment',
                'codigo_latitude': '0',
                'codigo_longitude': '0',
                'line_number': line,
                'terminal': '1',
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
            "/realizar_post/?line_number=0.001&busline_id=1")
        self.assertEquals(response.status_code, STATUS_OK)

    @patch('django.test.Client.post')
    def test_make_post_twitter(self, mock_get):
        mock_response = Mock()
        mock_response.return_value = True
        mock_get.return_value = mock_response
        self.client.post(
            "realizar_post/", self.post_data('1', '1', "0", "bom1", '0.001'))

        mock_get.assert_called_once_with(
            "realizar_post/", self.post_data('1', '1', "0", "bom2", '0.001'))
        mock_response.assert_called_once()

    @patch('django.test.Client.post')
    def test_make_post_action_with_user(self, mock_get):
        mock_response = Mock()
        mock_response.return_value = True
        mock_get.return_value = mock_response
        self.create_user()
        self.client.login(username='test_user', password='test_password')

        self.client.post(
            "/realizar_post/", self.post_data('2', '2', '0', "bom3", '0.003'))
        mock_get.assert_called_once_with(
            "/realizar_post/", self.post_data('2', '2', "0", "bom3", '0.003'))
        mock_response.assert_called_once()
        self.client.logout()
        self.user.delete()

    @patch('django.test.Client.post')
    def test_make_post_action_with_user_and_line(self, mock_get):
        mock_response = Mock()
        mock_response.return_value = True
        mock_get.return_value = mock_response
        self.create_busline()
        self.create_user()
        self.client.login(username='test_user', password='test_password')
        self.client.post(
            "/realizar_post/", self.post_data('3', '3', '0', "bom4", '0.004'))
        mock_get.assert_called_once_with(
            "/realizar_post/", self.post_data('3', '3', "0", "bom4", '0.004'))
        mock_response.assert_called_once()
        self.client.logout()

    @patch('django.test.Client.post')
    def test_make_post_action_page_no_review(self, mock_get):
        mock_response = Mock()
        mock_response.return_value = True
        mock_get.return_value = mock_response
        self.create_user()
        self.client.login(username='test_user', password='test_password')
        self.client.post(
            "/realizar_post/", self.post_data('4', '4', '', "bom5", '0.005'))
        mock_get.assert_called_once_with(
            "/realizar_post/", self.post_data('4', '4', '', "bom5", '0.005'))
        mock_response.assert_called_once()
        self.client.logout()

    @patch('django.test.Client.post')
    def test_make_post_action_page_no_geolocation(self, mock_get):
        mock_response = Mock()
        mock_response.return_value = True
        mock_get.return_value = mock_response
        self.create_user()
        self.client.login(username='test_user', password='test_password')
        self.client.post(
            "/realizar_post/", self.post_data('5', '5', '0', "bom6", '0.006'))
        mock_get.assert_called_once_with(
            "/realizar_post/", self.post_data('5', '5', "0", "bom6", '0.006'))
        mock_response.assert_called_once()
        self.client.logout()
