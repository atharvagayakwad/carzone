from django.contrib import admin

from pages.models import TeamsModel
from django.utils.html import format_html

class TeamsAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50%;" />'.format(object.photo.url))

    thumbnail.short_description = "Photo"

    list_display = ('thumbnail', 'first_name', 'last_name', 'designation', 'created_date')
    list_display_links = ('first_name', 'last_name','thumbnail')
    search_fields = ('first_name', 'last_name','designation')
    list_filter = ('designation',)

# Register your models here.
admin.site.register(TeamsModel, TeamsAdmin)