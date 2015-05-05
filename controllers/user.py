# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from models.user import User


def register_user_page(request):
    User.filter_by_username(request.POST["username"])
    return render_to_response('register.html')


def register_user(request):
    user = User()
    user.first_name = request.GET["name"]
    user.email = request.GET["email"]
    user.username = request.GET["username"]
    user.set_password(request.GET["password"])
    user.save()
    return render_to_response("login.html")
