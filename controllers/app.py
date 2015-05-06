from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
# from django.contrib.auth.decorators import login_required


def login(request):
    if request.user.is_authenticated():
        response = redirect("/",
                            context_instance=RequestContext(request))

    else:
        response = render_to_response('login.html',
                                      context_instance=RequestContext(request))

    return response


# @login_required
def feed_page(request):
    return render_to_response('feed_page.html',
                              context_instance=RequestContext(request))

# def account_page(request):
    # return render_to_response('account.html',
    # context_instance=RequestContext(request)) #url
