# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from models.busline import Busline
# from api.busline import BuslineAPI
# from api import BuslineAPI
from django.template import RequestContext
from django.shortcuts import redirect


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

        response = render_to_response(
            "search_result_page.html", htmlvars,
            context_instance=RequestContext(request))
    else:
        response = render_to_response("search_result_page.html",
                                      {'buslines': buslines},
                                      context_instance=RequestContext(request))

    return response


def advanced_search_line(request):
    buslines = Busline.filter_by_multiple(
        line_number=request.GET['busline'],
        description=request.GET['description'],
        terminals=request.GET['terminals']
    )

    if(len(request.GET['busline']) == 0) and (len(request.GET['description']) == 0) and (len(request.GET['terminals']) == 0):
        return redirect("search_result_page", mensage_erro("Erro :(", "Todos os campos em branco",
                                                           "busca deve ser feita com pelo menos um campo preenchido"))
    else:
        return render_to_response("search_result_page.html",
                                  {'buslines': buslines},
                                  context_instance=RequestContext(request))


def advanced_search_page(request):
    return render_to_response("advanced_search_busline.html",
                              context_instance=RequestContext(request))


def mensagem_erro(mensagem_titulo, mensagem_sub_titulo, mensagem):
    htmlvars = {}
    htmlvars["mensagem1"] = mensagem_titulo
    htmlvars["mensagem2"] = mensagem_sub_titulo
    htmlvars["mensagem3"] = mensagem
    return htmlvars
