from models.terminal import Terminal
from models.busline import Busline
from models.line_sugested import LineSugested
from django.test import SimpleTestCase, Client

STATUS_OK = 200
STATUS_REDIRECT = 302


class Test_Line_Sugest(SimpleTestCase):

    def create_terminal(self):
        terminal = Terminal()
        terminal.description = "description"
        terminal.address = "address"
        terminal.save()
        return terminal

    def createsugested_line(self, description, justify, line_number):
        terminal = self.create_terminal()
        line_sugest = LineSugested()
        line_sugest.description = description
        line_sugest.justify = justify
        line_sugest.terminal = terminal
        line_sugest.save()
        return line_sugest    

    def test_sugest_line_page_get(self):
        response = self.client.get(
            "/sugerir/linha/")
        self.assertEquals(response.status_code, STATUS_OK)

    def test_sugest_line_page_post(self):
        db_before = LineSugested.objects.all()
        data = {'busline': '0.001',
                'description': 'comment',
                '': '0',
                'codigo_longitude': '0',
                'line_number': '0.001',
                'justify': '1',
                'via': 'epnb',
                'terminal': 10,
                }
        self.client.post("/sugerir/linha/", data)
        db_after = LineSugested.objects.all()
        self.assertTrue(db_after != db_before)
