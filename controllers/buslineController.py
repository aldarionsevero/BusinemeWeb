# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from models.busline import Busline
# from api import BuslineAPI
from django.template import RequestContext


def register_busline(request):

    busline = Busline()
    busline.line_number = request.POST['line_number']  # GET or POST?
    busline.description = request.POST['description']
    busline.via = request.POST['via']
    busline.route_size = request.POST['route_size']
    busline.fee = request.POST['fee']
    busline.company = request.POST['company']
    busline.terminals = request.POST['terminals']
    busline.save()
    return render_to_response('nameOfPage')

    # 1) Include in nameOfpage for
    #    where busline going to after save in db
    # 2) Create a new html, if necessary.
    # 3) include the new html page in 'urls.py'


def search_line(request):
    buslines = Busline.filter_by_line_number(request.POST['busline'])
    if len(request.POST['busline']) == 1:
        htmlvars = {}
        htmlvars["alert_title"] = "Erro :("
        htmlvars["error_lead"] = "Busca com menos de 2 digitos"
        htmlvars[
            "error_message"
        ] = "A busca deve ser feita com no minimo 2 digitos."
        htmlvars["count_busline"] = 0

        response = render_to_response(
            "search_result_page.html", htmlvars,
            context_instance=RequestContext(request))
    else:
        count_busline = len(buslines)
        response = render_to_response("search_result_page.html",
                                      {'buslines': buslines,
                                          'count_busline': count_busline},
                                      context_instance=RequestContext(request))

    return response
