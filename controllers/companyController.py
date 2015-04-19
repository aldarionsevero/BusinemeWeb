# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from company.py import Company


def register_company(request):

    company = Company()
    company.name = request.POST['name']
    company.save()

    return render_to_response('nameOfPage')

    # 1) Include in nameOfpage for
    #    where busline going to after save in db
    # 2) Create a new html, if necessary.
    # 3) include the new html page in 'urls.py'
