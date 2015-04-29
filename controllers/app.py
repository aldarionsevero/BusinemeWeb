from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


def login(request):
    return render_to_response('login.html', context_instance=RequestContext(request))


#@login_required
def feed_page(request):
    return render_to_response('feed.html', context_instance=RequestContext(request))
