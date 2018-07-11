from django.contrib import admin

from .models import Url, Log

class UrlAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'keyword', 'origin_url']
    list_display_links = ['id', 'title']
    #
    readonly_fields = ('clicks', 'timestamp')
    fieldsets = [
        ('Url Information', {
            'fields': ['keyword', 'origin_url', 'title']
            }),
        ('Other', {
            'fields': ['category', 'tags'],
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