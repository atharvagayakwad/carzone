from django.contrib import admin
from django.utils.html import format_html

from cars.models import CarsModel

class CarAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40"  />'.format(object.car_photo_1.url))

    thumbnail.short_description = "Car Image"

    list_display = ('thumbnail','car_title','city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('thumbnail', 'car_title')
    list_editable = ( 'is_featured',)
    search_fields = ('car_title', 'city', 'color', 'model', 'body_style','fuel_type')
    list_filter = ('city', 'color', 'model', 'body_style','fuel_type')
    
# Register your models here.
admin.site.register(CarsModel,CarAdmin)
