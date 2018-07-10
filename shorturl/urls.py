""" App shorturl URL Configuration
"""

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    # Route shorturl
    # eg. /abc, keyword = 'abc'
    re_path(r'^(?P<keyword>[\w][\w-]+)$', views.go_to_origin),
]