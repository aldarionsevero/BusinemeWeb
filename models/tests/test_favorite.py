from django.test import SimpleTestCase
from models.busline import Busline
from models.user import User
from models.terminal import Terminal
from models.favorite import Favorite


class TestFavorite (SimpleTestCase):

    def setup(self):
        Favorite.objects.all().delete()
        User.objects.all().delete()
        BUsline.objects.all().delete()

    def create_busline(self, line_number):
        busline = Busline()
        busline.line_number = line_number
        busline.description = "description"
        busline.via = "via"
        busline.route_size = 2.5
        busline.fee = 2.0
        terminal = Terminal(description="terminal")
        terminal.save()
        busline.save()
        busline.terminals.add(terminal)
        return busline

    def create_user(self, username):
        user = User()
        user.username = username
        user.password = '66786'
        user.name = 'test_name'
        user.email = 'test@email.tes'
        user.save()
        return user

    def create_favorite(self, username, line_number):
        favorite = Favorite()
        favorite.user = self.create_user(username)
        favorite.busline = self.create_busline(line_number)
        return favorite

    def test_all(self):
        self.create_favorite('josefina', '001')
        favorites = Favorite.all()
        self.assertEquals(1, len(favorites))

    def test_favorites(self):
        self.create_favorite('joao', '002')
        favorites = Favorite.favorites(self.iduser_get('joao'))
        self.assertEquals(1, len(favorites))

    def iduser_get(self, username):
        user = User.filter_by_username(username)
        useri = user.id
        return useri

    def test_isfavorite(self):
        self.create_favorite('jose', '004')
        self.assertTrue(Favorite.is_favorite(1, 1))

    def test_deletefavorite(self):
        self.create_favorite('joaquim', '005')
        db_before = Favorite.all()
        Favorite.delete_favorite(1, 1)
        db_after = Favorite.all()
        self.assertTrue(db_before != db_after)
