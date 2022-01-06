from django.contrib import admin

from .models import URL


class URLAdmin(admin.ModelAdmin):
    list_display = ('id', 'shorted_url', 'full_url', 'author', 'create_date')
    list_display_links = ('id', 'shorted_url')
    search_fields = ('author', )


admin.site.register(URL, URLAdmin)
