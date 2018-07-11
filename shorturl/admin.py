from django.contrib import admin

from .models import Url, Log

class UrlAdmin(admin.ModelAdmin):
    readonly_fields = ['creator', 'creator_ip', 'timestamp']
    fieldsets = [
        ('Url Information', {
            'fields': ['keyword', 'origin_url', 'title']
            }),
        ('Clicks', {'fields': ['clicks']}),
        ('Creator Information', {'fields': readonly_fields})
    ]
admin.site.register(Url, UrlAdmin)

admin.site.register(Log)