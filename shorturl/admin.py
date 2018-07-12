from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Url, Log

# AdminSite Title and Header
class ShorturlAdminSite(AdminSite):
    site_header = "ShortUrl Admin"
    site_title = "ShortUrl Admin"

class UrlAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'keyword', 'origin_url', 'permanent']
    list_display_links = ['id', 'title']
    #
    readonly_fields = ('clicks', 'timestamp')
    fieldsets = [
        ('Url Information', {
            'fields': ['keyword', 'origin_url', 'title']
            }),
        ('Other', {
            'fields': ['category', 'tags', 'permanent'],
            'classes': ['collapse']
        }),
        (None, {'fields': readonly_fields}),
    ]

class LogAdmin(admin.ModelAdmin):
    list_display = ['id', 'url', 'click_timestamp', 'click_ip', 'referrer', 'user_agent']
    list_display_links = ['id']
    #
    readonly_fields = ['url', 'click_timestamp', 'click_ip', 'referrer', 'user_agent']

admin.site.register(Url, UrlAdmin)
admin.site.register(Log, LogAdmin)

admin_site = ShorturlAdminSite(name='urladmin')
admin_site.register(Url, UrlAdmin)
admin_site.register(Log, LogAdmin)