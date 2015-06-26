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
from configuration import security
from twython import Twython

capacity_dictionary = {1: "OnibusVazio",
                       2: "ComPoucosAssentosVagos",
                       3: "SemAssentosVagos",
                       4: "OnibusCheio",
                       5: "OnibusLotado"}

traffic_dictionary = {1: "TransitoLivre",
                      2: "ComPontosdeRetencao",
                      3: "LevementeEngarrafado",
                      4: "TransitoEngarrafado",
                      5: "TransitoParado"}


def make_post_page(request):
    """Return the post page when requested. """
    line_number = request.GET['line_number']
    busline_id = request.GET['busline_id']
    busline = Busline.filter_by_line_equals(line_number)
    terminals = busline.terminals
    try:
        last_post = Post.last(busline_id)
    except LineWithoutPostError:
        last_post = None
    if request.user.is_authenticated():
        return render_to_response("make_post_page.html",
                                  {'line_number': line_number,
                                   'last_post': last_post,
                                   'terminals': terminals},
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
    post.capacity = int(request.POST['capacity'])
    post.traffic = int(request.POST['traffic'])
    post.comment = request.POST['description']
    post.latitude = request.POST['codigo_latitude']
    post.longitude = request.POST['codigo_longitude']
    post.user_id = request.user.id
    post.terminal_id = request.POST["terminal"]
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

        post_twitter(request.POST['line_number'], post.capacity, post.traffic)

        if post.latitude == "" or post.longitude == "":
            return modal_message('Erro :(', 'Serviço não disponível',
                                 'Não conseguimos obter sua geolocalização',
                                 'feed_page.html', request)
        post.save()

        response = modal_message('Sucesso', 'Post realizado', 'Post realizado \
            com sucesso!', 'feed_page.html', request)

    except ApiException:
        response = modal_message('Erro :(', 'Servidor não disponível', 'O \
        acesso ao servidor está indisponível no momento, verifique sua \
        conexão', 'login_page.html', request)

    return response


def post_twitter(line_number, capacity, traffic):
    post_line_number = line_number
    post_line_number = post_line_number.replace('.', '')
    APP_KEY = security.TWITTER_CONSUMER_KEY
    APP_SECRET = security.TWITTER_CONSUMER_SECRET
    OAUTH_TOKEN = security.TWITTER_ACCESS_TOKEN_KEY
    OAUTH_TOKEN_SECRET = security.TWITTER_ACCESS_TOKEN_SECRET
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    message = '#Busine%s #%s  #%s' % \
        (post_line_number, capacity_dictionary[
         capacity], traffic_dictionary[traffic])
    tweet_posted = twitter.update_status(status=message)
    return tweet_posted


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
