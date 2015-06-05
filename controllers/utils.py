from django.shortcuts import render_to_response
from django.template import RequestContext


def error_message(alert_title, error_lead, error_message, html, request):
    htmlvars = {}
    htmlvars["alert_title"] = alert_title
    htmlvars["error_lead"] = error_lead
    htmlvars["error_message"] = error_message
    response = response_htmlvars(htmlvars, html, request)
    return response


def response_htmlvars(htmlvars, html, request):
    response = render_to_response(html, htmlvars,
                                  context_instance=RequestContext(request))
    return response
