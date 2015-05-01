# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from django.template.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse


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


@login_required
def logout_user(request):
    logout(request)
    return redirect('/login/', context_instance=RequestContext(request))


@login_required
def user_account(request):
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    return render_to_response('account.html', {'user': user},
                              context_instance=RequestContext(request))


@login_required
def change_password_page(request):
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    return render_to_response('change_password_page.html', {'user': user},
                              context_instance=RequestContext(request))


@login_required
def change_password(request):
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None

    old_password = request.POST["old_password"]
    new_password1 = request.POST["new_password1"]
    new_password2 = request.POST["new_password2"]

    if not user.check_password(old_password):
        response = HttpResponse("Sua senha antiga está incorreta.")
    else:
        if not (new_password1 == new_password2):
            response = HttpResponse("Sua senha nova não bate com a comparação")
        else:
            user.set_password(new_password1)
            user.save()
            response = redirect("/login/",
                                context_instance=RequestContext(request))
            logout(request)
    return response


@login_required
def change_userdata(request):
    # Try to change the data of the usere
    if request.user.is_authenticated():
        user = request.user
        user.first_name = request.POST["name"]
        user.email = request.POST["email"]
        user.username = request.POST["username"]
        user.save()
    return redirect("/",
                    context_instance=RequestContext(request))


@login_required
def delete_account_page(request):
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    return render_to_response('delete_account_page.html', {'user': user},
                              context_instance=RequestContext(request))


@login_required
def delete_account(request):
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None

    password = request.POST["password"]

    if not user.check_password(password):
        response = HttpResponse("Sua senha está incorreta.")
    else:
        user.delete()
        response = redirect("/login/",
                            context_instance=RequestContext(request))
        logout(request)
    return response
