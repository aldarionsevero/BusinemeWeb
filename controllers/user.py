# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# from django.template.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import redirect


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


def log_user(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/', context_instance=RequestContext(request))
            # return render_to_response('feed_page.html', context_instance=RequestContext(request))
        # else:
        # return disable acoount
    # else:
        # invalid login
