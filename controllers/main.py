from django.shortcuts import render_to_response


def main():
    """Load main page."""
    return render_to_response('main.html')
