# -*- coding: utf-8 -*-

from django.test import SimpleTestCase
from api.models.busline import Busline as ApiBusline
from models.post import Post


class BuslineTest(SimpleTestCase):

    def create_post(self):
        post = Post()
        post.comment = 'comentario'
        post.latitude = '0'
        post.longitude = '0'
        post.traffic = '3'
        post.capacity = '3'
        post.date = '01/01/01'
        post.time = '00:00'
        post.save()
        return post

    def test_post_all(self):
        self.create_post()
        posts = Post.all()
        self.assertEquals(1, len(posts))
