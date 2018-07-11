from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Url, Log

def index(requests):
    return HttpResponse('Hello from Shorturl. This is a simple url shortner by Jinpeng.' + requests.user.get_username())

# Redirect to origin URL
def go_to_origin(requests, keyword):
    item = get_object_or_404(Url, keyword=keyword)
    # Url.clicks add 1
    item.clicked()
    # Return http301 redirect
    return redirect(item.origin_url, permanent=True)