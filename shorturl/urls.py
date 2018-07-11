""" App shorturl URL Configuration
"""

from django.urls import path, re_path
from . import views

app_name = 'shorturl'

urlpatterns = [
    # Route shorturl
    # eg. /abc, keyword = 'abc'
    re_path(r'^(?P<keyword>[\w]+[\w-]*)$', views.go_to_origin),
    re_path(r'^$', views.index),
]