from django.contrib import admin

from .models import Pug, Team


@admin.register(Pug)
class PugAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'owner',
        'name',
        'guild',
        'text_channel',
        'status'
    ]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'pug',
        'name',
        'captain'
    ]
