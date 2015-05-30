# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from models.busline import Busline
# from api import BuslineAPI
from django.template import RequestContext
# from django.shortcuts import redirect
from controllers.utils import error_message


def search_line(request):
    line_number = request.GET['busline']
    buslines = Busline.filter_by_line_number(line_number)
    count_busline = len(buslines)
    response = render_to_response("search_result_page.html",
                                  {'buslines': buslines,
                                   'count_busline': count_busline,
                                   'searched_number': line_number},
                                  context_instance=RequestContext(request))

    return response


def advanced_search_line(request):

    if ((len(request.GET['busline']) < 2) and
            (len(request.GET['description']) < 2) and
            (len(request.GET['terminal__description']) < 2)):
        response = error_message(
            "Erro :(", "Busca com apenas um dígito", "A busca deve ser \
                realizada com no mínimo 2 dígitos ou apenas \
        vazia para vizualizar todas as linhas.",
            "search_result_page.html", request)
    else:
        buslines = Busline.filter_by_multiple(
            line_number=request.GET['busline'],
            description=request.GET['description'],
            terminal__description=request.GET['terminal__description']
        )
        count_busline = len(buslines)
        line_number=request.GET['busline']
        response = render_to_response("search_result_page.html",
                                      {'buslines': buslines,
                                       'count_busline': count_busline,
                                       'searched_number':line_number},
                                      context_instance=RequestContext(request))
    return response


def advanced_search_page(request):
    return render_to_response("advanced_search_busline.html",
                              context_instance=RequestContext(request))
