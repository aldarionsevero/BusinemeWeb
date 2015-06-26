# -*- coding: utf-8 -*-
from django.template import RequestContext
from controllers.utils import call_feed_page
from models.terminal import Terminal
from models.line_sugested import LineSugested
from django.shortcuts import render_to_response


def sugesting_line(request):
    r"""
    Call method to sugest_line  depending on the request \
    method (GET or POST).
    """
    if request.method == 'GET':
        response = sugesting_line_page(request)
    elif request.method == 'POST':
        response = sugesting_line_action(request)
    return response


def sugesting_line_page(request):
    terminals = Terminal.all()
    response = render_to_response('line_sugested_page.html', {
                                  'terminals': terminals},
                                  context_instance=RequestContext(request))
    return response


def sugesting_line_action(request):
    """save data on db page when requested. """
    line_sugest = LineSugested()
    line_sugest.busline = request.POST['busline']
    line_sugest.description = request.POST['description']
    line_sugest.justify = request.POST['justify']
    line_sugest.via = request.POST['via']
    line_sugest.terminal_id = request.POST['terminal']
    # line_sugest.terminal = request.POST['terminal']
    line_sugest.save()

    response = call_feed_page(request,
                              alert_title='Sucesso',
                              error_lead='linha sugerida com sucesso',
                              modal_message='Uma nova linha foi sugerida e \
        será avalida pela nossa equipe! Obrigado pela\
          sugestão!')
    return response
