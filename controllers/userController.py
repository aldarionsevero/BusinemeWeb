# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from models.user import User
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from controllers.utils import error_message


def register_user_page(request):
    r"""
    Loads the register user page. If a user is authenticated, it will be \
    redirected to the main page instead
    """
    if request.user.is_authenticated():
        response = redirect("/",
                            context_instance=RequestContext(request))
    else:
        response = render_to_response('register.html',
                                      context_instance=RequestContext(request))
    return response


def register_user(request):
    r"""
    Registers the user if all the data inserted in the forms are valid. The \
    email has to be unique, and with "@" and a "." (dot). The username has to \
    be unique. Finally, no fields can be blank.
    """
    # c = {}
    # c.update(csrf(request))
    user = User()
    user.first_name = request.POST["name"]
    user.email = request.POST["email"]
    user.username = request.POST["username"]
    user.set_password(request.POST["password"])
    try:
        if not user.validate_unique_email():
            response = error_message(
                "Erro :(",
                "Email ja cadastrado.", "O e-mail inserido já \
                está em uso. Utilize um e-mail diferente para realizar o \
                cadastro.",
                "register.html", request)
            return response
        response = redirect("/login/",
                            context_instance=RequestContext(request))
        if not user.validate_email():
            response = error_message(
                "Erro :(",
                "E-mail inválido.",
                "Verifique o e-mail inserido. Ele deve conter os caracteres '@'\
                 e '.' (ponto).",
                "register.html", request)
        if not user.validade_user_password(request.POST["password"]):
            response = error_message(
                "Erro :(",
                "Campo de senha vazio.",
                "Não é possível realizar o cadastro com a senha vazia, insira\
                 uma por favor.",
                "register.html", request)

        if user.validate_email() and user.validate_unique_email() and \
                user.validade_user_password(request.POST["password"]):
            user.save()

    except IntegrityError:
        if not user.validate_user_name():
            response = error_message(
                "Erro :(",
                "Usuário já cadastrado.",
                "O nome de usuário inserido já está em uso.",
                "register.html", request)

    return response


def log_user(request):
    r"""
    Calls method to log the user depending on the input method (GET or POST).
    """
    if request.method == 'GET':
        response = log_user_get(request)
    elif request.method == 'POST':
        response = log_user_post(request)
    return response


def log_user_get(request):
    r"""
    Logs the user with GET method.
    """
    if request.user.is_authenticated():
        response = redirect("/",
                            context_instance=RequestContext(request))
    else:
        response = render_to_response('login.html',
                                      context_instance=RequestContext(request))
    return response


def log_user_post(request):
    r"""
    Logs the user with POST method. Checks if user is deactivated and if \
    username or password are incorrect.
    """
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            response = redirect('/', context_instance=RequestContext(request))
        else:
            response = error_message(
                "Erro :(",
                "Usuário desativado.",
                "Esta usuário foi desativado.\
            Entre em contato com o suporte Busine.me para solicitar a\
             reativação.",
                "login.html", request)
    else:
        response = error_message(
            "Erro :(",
            "Usuário não encontrado.",
            "Verifique se o nome de usuário e a senha informados estão\
             corretos.",
            "login.html", request)
    return response


@login_required
def logout_user(request):
    r"""
    Logs user out
    """
    logout(request)
    return redirect('/login/', context_instance=RequestContext(request))


@login_required
def user_account(request):
    r"""
    Loads the account managment page, that lets the user change his data.
    """
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    return render_to_response('account.html', {'user': user},
                              context_instance=RequestContext(request))


@login_required
def change_password_page(request):
    r"""
    Loads the password managment page, that lets the user change his password.
    """
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    return render_to_response('change_password_page.html', {'user': user},
                              context_instance=RequestContext(request))


@login_required
def change_password(request):
    r"""
    Changes user password checking for his current password.
    """
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None

    old_password = request.POST["old_password"]
    new_password1 = request.POST["new_password1"]
    new_password2 = request.POST["new_password2"]

    if not user.check_password(old_password):
        response = error_message(
            "Erro :(",
            "Senha atual incorreta.",
            "Verifique a escrita da senha informada.",
            "login.html", request)
    else:
        if not (new_password1 == new_password2):
            response = error_message(
                "Erro :(",
                "Os campos de nova senha não conferem.",
                "Verifique a escrita das senhas informadas.",
                "login.html", request)
        else:
            user.set_password(new_password1)
            user.save()
            response = redirect("/login/",
                                context_instance=RequestContext(request))
            logout(request)
    return response


@login_required
def change_userdata(request):
    r"""
    Changes user data.
    """
    # Try to change the data of the usere
    if request.user.is_authenticated():
        user = request.user
        user.first_name = request.POST["name"]
        user.email = request.POST["email"]
        user.save()
    return redirect("/",
                    context_instance=RequestContext(request))


@login_required
def deactivate_account_page(request):
    r"""
    Loads user account deactivation page.
    """
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    return render_to_response('deactivate_account_page.html', {'user': user},
                              context_instance=RequestContext(request))


@login_required
def deactivate_account(request):
    r"""
    Deactivates user account checking for his current password.
    """
    user = request.user

    password = request.POST["password"]

    if not user.check_password(password):
        response = error_message(
            "Erro :(",
            "Senha incorreta.",
            "Verifique a escrita da senha informada.",
            "deactivate_account_page.html", request)
    else:
        user.is_active = False
        user.save()
        logout(request)
        response = error_message(
            "Sucesso!",
            "Usuário desativado com sucesso.",
            "Esperamos o seu retorno, até logo! :)",
            "login.html", request)
    return response
