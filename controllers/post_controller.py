# -*- coding: utf-8 -*-
"""Post controller docstring"""
from django.shortcuts import render_to_response
from models.post import Post
from django.template import RequestContext
from api.busline import BuslineAPI
from controllers.utils import modal_message
from exception.api import ApiException
from django.contrib.auth.decorators import login_required
from exception.line_without_post import LineWithoutPostError


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
    api = BuslineAPI()
    try:
        busline = api.filter_by_line_equals(request.POST['line_number'])
        post.busline_id = busline.id
        post.save()
        response = modal_message('Sucesso', 'Post realizado', 'Post realizado \
            com sucesso!', 'login_page.html', request)
    except ApiException, e:
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
