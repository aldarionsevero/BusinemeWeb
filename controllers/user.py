# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# from django.template.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import redirect
# from exception.existing_user import ExistingUser
from django.db import IntegrityError


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
    html_vars = {}
    try:
        user.save()
    except IntegrityError:
        html_vars["error"] = "teste"

    if html_vars:
        response = render_to_response("register.html", html_vars,
                                      context_instance=RequestContext(request))
    else:
        response = redirect("/login/",
                            context_instance=RequestContext(request))
    return response


def log_user(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/', context_instance=RequestContext(request))
        # else:
        # return disable acoount
    # else:
        # invalid login


def user_account(request):
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    return render_to_response('account.html', {'user': user},
                              context_instance=RequestContext(request))


def change_password(request):
    return render_to_response('change_password_page.html', {'user': user},
                              context_instance=RequestContext(request))
