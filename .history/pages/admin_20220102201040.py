from django.contrib import admin
from .models import Team
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'designation', 'created_date')
    list_display_links = ('id', 'first_name')

admin.site.register(Team, TeamAdmin)
