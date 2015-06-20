from django.shortcuts import render_to_response
from django.template import RequestContext


def feed_page(request):
    """Load feed page."""
    return render_to_response('feed_page.html',
                              context_instance=RequestContext(request))


def about_page(request):
    """Load about page."""
    return render_to_response('about_page.html',
                              context_instance=RequestContext(request))
