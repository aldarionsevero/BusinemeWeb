# -*- coding: utf-8 -*-
"""Post controller docstring"""
from django.shortcuts import render_to_response, redirect
from models.post import Post
from django.template import RequestContext
from api.busline import BuslineAPI


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


def make_post_page(request):
    """Return the post page when requested. """
    line_number = request.GET['line_number']
    return render_to_response("make_post_page.html",
                              {'line_number': line_number},
                              context_instance=RequestContext(request))


def make_post(request):
    post = Post()
    post.capacity = request.POST['capacity']
    post.traffic = request.POST['traffic']
    post.comment = request.POST['description']
    post.latitude = str(request.POST.get('codigo_latitude'))
    post.longitude = str(request.POST.get('codigo_longitude'))

    api = BuslineAPI()
    busline = api.filter_by_line_equals(request.POST['line_number'])
    post.busline_id = busline.id
    post.save()

    return redirect(
        "/",
        context_instance=RequestContext(request))
