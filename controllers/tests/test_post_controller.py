from django.test import SimpleTestCase, Client
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
        self.create_busline()
        self.create_user('username')

    def create_user(self, username):
        self.user = User()
        self.user.username = username
        self.user.set_password('test_password')
        self.user.name = 'test_name'
        self.user.email = 'test@email.tes'
        self.user.save()

    def create_busline(self):
        self.busline = Busline()
        self.busline.line_number = "001"
        self.busline.description = "description"
        self.busline.via = "via"
        self.busline.route_size = 2.5
        self.busline.fee = 2.0
        self.terminal = Terminal(description="terminal")
        self.terminal.save()
        self.busline.save()
        self.busline.terminals.add(self.terminal)
        return self.busline

    def post_data(self, codigo_latitude, codigo_longitude, review):
        data = {'capacity': '5',
                'traffic': '5',
                'description': 'comment',
                'codigo_latitude': codigo_latitude,
                'codigo_longitude': codigo_longitude,
                'line_number': '001',
                'review': review,
                'terminal': '1'}
        return data

    def test_make_post_page(self):
        response = self.client.get(
            "/realizar_post/?line_number=001&busline_id=01")
        self.assertEquals(response.status_code, STATUS_OK)

    def test_make_post_page_with_user(self):
        self.client.login(username='username', password='test_password')
        response = self.client.get(
            "/realizar_post/?line_number=001&busline_id=01")
        self.assertEquals(response.status_code, STATUS_OK)
        self.client.logout()
        self.user.delete()

    def test_make_post_action_with_user(self):
        self.client.login(username='username', password='test_password')
        response = self.client.post(
            "/realizar_post/", self.post_data('0', '0', '0'))
        self.assertEquals(response.status_code, STATUS_OK)
        self.client.logout()
        self.user.delete()

    def test_make_post_action_with_user_and_line(self):
        self.client.login(username='username', password='test_password')
        response = self.client.post(
            "/realizar_post/", self.post_data('0', '0', '0'))
        self.assertEquals(response.status_code, STATUS_OK)
        self.client.logout()
        self.user.delete()

    def test_make_post_action_page_no_review(self):
        self.client.login(username='username', password='test_password')
        response = self.client.post(
            "/realizar_post/", self.post_data('0', '0', ''))
        self.assertEquals(response.status_code, STATUS_OK)
        self.client.logout()
        self.user.delete()

    def test_make_post_action_page_no_geolocation(self):
        self.client.login(username='username', password='test_password')
        response = self.client.post(
            "/realizar_post/", self.post_data('', '', '0'))
        self.assertEquals(response.status_code, STATUS_OK)
        self.client.logout()
        self.user.delete()
