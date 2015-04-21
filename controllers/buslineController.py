# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from busline.py import Busline


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
