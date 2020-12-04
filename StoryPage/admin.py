from django.contrib import admin
from StoryPage.models import PlotPoint, Choice, User


@admin.register(PlotPoint)
class PlotPointAdmin(admin.ModelAdmin):
    list_display = ['id', 'pptext', 'writtenby', 'uv', 'dv']
    search_fields = ['pptext', 'id']


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'writtenby', 'uv', 'dv']
    search_fields = ['text', 'id']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    search_fields = ['username']
