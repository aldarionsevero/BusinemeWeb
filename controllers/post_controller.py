# -*- coding: utf-8 -*-
"""Post controller docstring"""
from django.shortcuts import render_to_response
from models.post import Post
from django.template import RequestContext
from api.busline import BuslineAPI
from controllers.utils import modal_message


def make_post_page(request):
    """Return the post page when requested. """
    line_number = request.GET['line_number']
    return render_to_response("make_post_page.html",
                              {'line_number': line_number},
                              context_instance=RequestContext(request))


def make_post_action(request):
    """Perform the action of saving the post. """
    post = Post()
    post.capacity = request.POST['capacity']
    post.traffic = request.POST['traffic']
    post.comment = request.POST['description']
    post.latitude = request.POST['codigo_latitude']
    post.longitude = request.POST['codigo_longitude']

    api = BuslineAPI()
    try:
        busline = api.filter_by_line_equals(request.POST['line_number'])
        post.busline_id = busline.id
        post.save()
        response = modal_message('Sucesso', 'Post realizado', 'Post realizado \
            com sucesso!', 'login_page.html', request)
    except:
        response = modal_message('Erro :(', 'Servidor não disponível', 'O \
            acesso ao servidor está indisponível no momento, verifique sua \
            conexão', 'login_page.html', request)

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
