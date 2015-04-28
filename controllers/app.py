from django.shortcuts import render_to_response


def login(request):
    return render_to_response('login.html')


def feed_page(request):
    return render_to_response('feed.html')
