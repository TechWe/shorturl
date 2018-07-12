from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Url, Log

def index(requests):
    get_header = lambda meta, header, default: meta[header] if header in meta else default
    meta = requests.META
    ip = get_header(meta, 'REMOTE_ADDR', '0.0.0.0')
    referrer = get_header(meta, 'HTTP_REFERER', 'direct')
    user_agent = get_header(meta, 'HTTP_USER_AGENT', '')

    return HttpResponse(f'Hello from Shorturl. This is a simple url shortner by Jinpeng. \n{ip} \n{referrer} \n{user_agent}')

# Redirect to origin URL
def go_to_origin(requests, keyword):
    item = get_object_or_404(Url, keyword=keyword)
    # Url.clicks add 1
    item.clicked()
    #
    get_header = lambda meta, header, default: meta[header] if header in meta else default
    meta = requests.META
    ip = get_header(meta, 'REMOTE_ADDR', '0.0.0.0')
    referrer = get_header(meta, 'HTTP_REFERER', 'direct')
    user_agent = get_header(meta, 'HTTP_USER_AGENT', '')
    log = Log(url=keyword, click_ip=ip, referrer=referrer, user_agent=user_agent)
    log.save()
    # Return http301 redirect
    return redirect(item.origin_url, permanent=item.permanent)