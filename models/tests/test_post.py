# -*- coding: utf-8 -*-

from django.test import SimpleTestCase
from models.busline import Busline
from models.terminal import Terminal
from models.post import Post


class BuslineTest(SimpleTestCase):

    def setUp(self):
        Busline.objects.all().delete()

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

    def create_post(self):
        busline = self.create_busline()
        post = Post()
        post.comment = 'comentario'
        post.latitude = '0'
        post.longitude = '0'
        post.traffic = '3'
        post.capacity = '3'
        post.date = '01/01/01'
        post.time = '00:00'
        post.busline = busline
        post.save()
        return post

    def test_post_all(self):
        self.create_post()
        posts = Post.all()
        self.assertEquals(1, len(posts))
