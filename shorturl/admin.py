from django.contrib import admin

from .models import Url, Log

admin.site.register(Url)
admin.site.register(Log)