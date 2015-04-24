# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
# from django.template.context_processors import csrf
from django.template import RequestContext


def register_user_page(request):
    return render_to_response('register.html',
                              context_instance=RequestContext(request))


def register_user(request):
    # c = {}
    # c.update(csrf(request))
    user = User()
    user.first_name = request.POST["name"]
    user.email = request.POST["email"]
    user.username = request.POST["username"]
    user.set_password(request.POST["password"])
    user.save()
    return render_to_response("login.html",
                              context_instance=RequestContext(request))
