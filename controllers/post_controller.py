# -*- coding: utf-8 -*-
"""Post controller docstring"""
from django.shortcuts import render_to_response
from models.post import Post
from models.busline import Busline
from django.template import RequestContext
from controllers.utils import modal_message
from django.contrib.auth.decorators import login_required
from exception.line_without_post import LineWithoutPostError
from exception.api import ApiException
from twitter.api import *


def make_post_page(request):
    """Return the post page when requested. """
    line_number = request.GET['line_number']
    busline_id = request.GET['busline_id']
    try:
        last_post = Post.last(busline_id)
    except LineWithoutPostError:
        last_post = None
    if request.user.is_authenticated():
        return render_to_response("make_post_page.html",
                                  {'line_number': line_number,
                                   'last_post': last_post},
                                  context_instance=RequestContext(request))
    else:
        return modal_message(
            "Erro :(",
            "Usuário não logado.",
            "Para realizar esta ação.\
             você deve estar logado.",
            "login_page.html", request)


@login_required
def make_post_action(request):
    """Perform the action of saving the post. """

    post = Post()
    post.capacity = request.POST['capacity']
    post.traffic = request.POST['traffic']
    post.comment = request.POST['description']
    post.latitude = request.POST['codigo_latitude']
    post.longitude = request.POST['codigo_longitude']
    post.user_id = request.user.id
    pontuation = 0
    if request.POST['review'] == '':
        pontuation = 0
    else:
        pontuation = int(request.POST['review'])
    try:
        busline = Busline.filter_by_line_equals(request.POST['line_number'])
        post.busline_id = busline.id
        try:
            last_post = Post.last(post.busline_id)
            last_post.user.pontuation = last_post.user.pontuation + \
                pontuation
            last_post.user.save()
        except LineWithoutPostError:
            pass

        post.save()
        t = Twitter(auth=OAuth(token, token_key, con_secret, con_secret_key))
        t.statuses.update(
            status="Using @sixohsix's sweet Python Twitter Tools.")
        # twitter = Twitter('businemeweb@gmail.com', 'busineme123')
        # twitter.statuses.update(status='I am tweeting from Python!')

        response = modal_message('Sucesso', 'Post realizado', 'Post realizado \
            com sucesso!', 'feed_page.html', request)
    except ApiException:
        response = modal_message('Erro :(', 'Servidor não disponível', 'O \
        acesso ao servidor está indisponível no momento, verifique sua \
        conexão', 'login_page.html', request)

    if post.latitude == "" or post.longitude == "":
        response = modal_message('Erro :(', 'Serviço não disponível',
                                 'Não conseguimos obter sua geolocalização',
                                 'feed_page.html', request)
    return response


def make_post(request):
    r"""
    Call method to make the post depending on the request \
    method (GET or POST).
    """
    if request.method == 'GET':
        response = make_post_page(request)
    elif request.method == 'POST':
        response = make_post_action(request)

    return response
