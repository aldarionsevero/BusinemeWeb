# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from models.user import User
from django.contrib.auth import authenticate, login, logout
# from django.template.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError


def register_user_page(request):
    if request.user.is_authenticated():
        response = redirect("/",
                            context_instance=RequestContext(request))
    else:
        response = render_to_response('register.html',
                                      context_instance=RequestContext(request))
    return response


def register_user(request):
    # c = {}
    # c.update(csrf(request))
    user = User()
    user.first_name = request.POST["name"]
    user.email = request.POST["email"]
    user.username = request.POST["username"]
    user.set_password(request.POST["password"])
    html_vars = {}
    htmlvars = {}
    try:
        if not user.validate_unique_email():
            htmlvars["alert_title"] = "Erro :("
            htmlvars["error_lead"] = "Email ja cadastrado."
            htmlvars[
                "error_message"
            ] = "O e-mail cadastrado já está em uso."
            response = render_to_response("register.html", htmlvars,
                                          context_instance=RequestContext(request))
            return response
        response = render_to_response("login.html", html_vars,
                                      context_instance=RequestContext(request))
        if not user.validate_email():
            htmlvars["alert_title"] = "Erro :("
            htmlvars["error_lead"] = "E-mail invalido."
            htmlvars[
                "error_message"
            ] = "E-mail invalido ."
            response = render_to_response("register.html", htmlvars,
                                          context_instance=RequestContext(request))
        user.save()
    except IntegrityError:
        if not user.validate_user_name():
            htmlvars["alert_title"] = "Erro :("
            htmlvars["error_lead"] = "Usuário ja cadastrado."
            htmlvars[
                "error_message"
            ] = "O nome de usuario escolhido ja esta em uso ."
            response = render_to_response("register.html", htmlvars,
                                          context_instance=RequestContext(request))

    return response


def log_user(request):
    if request.method == 'GET':
        response = log_user_get(request)
    elif request.method == 'POST':
        response = log_user_post(request)
    return response


def log_user_get(request):
    if request.user.is_authenticated():
        response = redirect("/",
                            context_instance=RequestContext(request))
    else:
        response = render_to_response('login.html',
                                      context_instance=RequestContext(request))
    return response


def log_user_post(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    htmlvars = {}
    if user is not None:
        if user.is_active:
            login(request, user)
            response = redirect('/', context_instance=RequestContext(request))
    else:

        htmlvars["alert_title"] = "Erro :("
        htmlvars["error_lead"] = "Usuário não encontrado."
        htmlvars[
            "error_message"
        ] = "Verifique se o nome de usuário e a senha informados estão corretos."
        response = render_to_response("login.html", htmlvars,
                                      context_instance=RequestContext(request))
    return response


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
    htmlvars = {}
    if not user.check_password(old_password):
        htmlvars["alert_title"] = "Erro :("
        htmlvars["error_lead"] = "Senha incorreta."
        htmlvars[
            "error_message"
        ] = "A senha antiga esta incorreta."
        response = render_to_response("change_password_page.html", htmlvars,
                                      context_instance=RequestContext(request))

    else:
        if not (new_password1 == new_password2):
            htmlvars["alert_title"] = "Erro :("
            htmlvars["error_lead"] = "Senha incorreta."
            htmlvars[
                "error_message"
            ] = "Os campos de nova senha nao conferem."
            response = render_to_response(
                "change_password_page.html", htmlvars,
                context_instance=RequestContext(request))
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
    htmlvars = {}
    user = request.user

    password = request.POST["password"]

    if not user.check_password(password):
        htmlvars["alert_title"] = "Erro :("
        htmlvars["error_lead"] = "Senha incorreta."
        htmlvars[
            "error_message"
        ] = "A senha está incorreta."
        response = render_to_response(
            "delete_account_page.html", htmlvars,
            context_instance=RequestContext(request))
    else:
        user.delete()
        htmlvars["alert_title"] = "Usuário deletado"
        htmlvars["error_lead"] = "Até logo"
        htmlvars[
            "error_message"
        ] = "Esperamos que você volte."
        logout(request)
        response = render_to_response(
            "login.html", htmlvars,
            context_instance=RequestContext(request))
    return response
