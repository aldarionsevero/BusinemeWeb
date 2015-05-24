# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from models.busline import Busline
# from api import BuslineAPI
from django.template import RequestContext
from django.shortcuts import redirect


def search_line(request):
    line_number = request.GET['busline']
    if len(line_number) == 1:
        htmlvars = {}
        htmlvars["alert_title"] = "Erro :("
        htmlvars["error_lead"] = "Busca com apenas um dígito"
        htmlvars[
            "error_message"
        ] = "A busca deve ser realizada com no mínimo 2 dígitos ou apenas vazia para vizualizar todas as linhas."

        response = redirect(
            request.META['HTTP_REFERER'], context_instance=RequestContext(request))
        # response = render_to_response(
        #     "search_result_page.html", htmlvars,
        #     context_instance=RequestContext(request))
    else:
        buslines = Busline.filter_by_line_number(line_number)
        count_busline = len(buslines)
        response = render_to_response("search_result_page.html",
                                      {'buslines': buslines,
                                          'count_busline': count_busline, 'searched_number': line_number},
                                      context_instance=RequestContext(request))

    return response


def advanced_search_line(request):
    buslines = Busline.filter_by_multiple(
        line_number=request.GET['busline'],
        description=request.GET['description'],
        terminals=request.GET['terminals']
    )

    if(len(request.GET['busline']) == 0) and (len(request.GET['description']) == 0) and (len(request.GET['terminals']) == 0):
        return redirect("search_result_page")
    else:
        return render_to_response("search_result_page.html",
                                  {'buslines': buslines},
                                  context_instance=RequestContext(request))


def advanced_search_page(request):
    return render_to_response("advanced_search_busline.html",
                              context_instance=RequestContext(request))
