from django.test import SimpleTestCase
from models.busline import Busline
from models.user import User
from models.terminal import Terminal
from models.favorite import Favorite


class TestFavorite (SimpleTestCase):

    def setup(self):
        pass

    def create_busline(self):
        Busline.objects.all().delete()
        busline = Busline()
        busline.line_number = "0.001"
        busline.description = "description"
        busline.via = "via"
        busline.route_size = 2.5
        busline.fee = 2.0
        terminal = Terminal(description="terminal")
        terminal.save()
        busline.save()
        busline.terminals.add(terminal)
        return busline

    def create_user(self):
        User.objects.all().delete()
        user = User()
        user.username = "test_test"
        user.set_password('1234')
        user.name = 'test_name'
        user.email = 'test@email.tes'
        user.save()
        return user

    def create_favorite(self):
        Favorite.objects.all().delete()
        favorite = Favorite()
        favorite.user = self.create_user()
        favorite.busline = self.create_busline()
        return favorite

    def test_all(self):
        Favorite.objects.all().delete()
        db_before = Favorite.all()
        favorite = self.create_favorite()
        favorite.save()
        db_after = Favorite.all()
        self.assertTrue(db_before != db_after)
