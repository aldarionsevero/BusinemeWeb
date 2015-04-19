# -*- coding: utf-8 -*-
from django.shorcuts import render_to_response
from post.py import Post


def register_post(request):
    post = Post()
    post.comment = request.POST['comment']
    post.position = request.POST['position']
    post.traffic = request.POST['traffic']
    post.capacity = request.POST['capacity']
    post.terminals = request.POST['terminals']
    post.date = request.POST['date']
    # This is a variable is already filled in automatically by
    # DateField.auto_now().
    post.time = request.POST['time']
    # This is a variable is already filled in automatically by
    # TimeField.auto_now().
    post.save()

    return render_to_response('nameOfPage')

    # 1) Include in nameOfpage for
    #    where busline going to after save in db
    # 2) Create a new html, if necessary.
    # 3) include the new html page in 'urls.py'
