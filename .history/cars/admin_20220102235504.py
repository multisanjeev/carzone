from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thambnail(self, object):
        return format_html('<img src={} width="40" style="border-radius:14px" />'.format(object.car_photo.url))
    
    thambnail.short_description = 'car image'
    list_display = ('id','thambnail','car_title','color','model', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('id', 'thambnail', 'car_title')
    list_editable = ('is_featured',)
    search_fields = ('car_title', 'city', 'model', 'body_style')

admin.site.register(Car, CarAdmin)
