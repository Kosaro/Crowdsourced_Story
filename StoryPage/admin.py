from django.contrib import admin
from Crowdsourced_Story.models import PlotPoint, Choice, User


@admin.register(PlotPoint)
class PlotPointAdmin(admin.ModelAdmin):
    list_display = ['pptext', 'writtenby', 'uv', 'dv']
    search_fields = ['pptext__startswith']


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['text', 'writtenby', 'uv', 'dv']
    search_fields = ['text__startswith']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    search_fields = ['username__startswith']
