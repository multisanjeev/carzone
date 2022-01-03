from django.contrib import admin
from .models import Car

# Register your models here.

def caradmin(admin.ModelAdmin):
    list_fields = ('car_title','color','model', 'body_type', 'fuel_type', 'is_featured')

admin.site.register(Car, caradmin)
