from django.contrib import admin
from StoryPage.models import *


@admin.register(PlotPoint)
class PlotPointAdmin(admin.ModelAdmin):
    list_display = ['pptext', 'writtenby', 'uv', 'dv']
    search_fields = ['pptext', 'id']
    id = models.AutoField(primary_key=True)

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['text', 'writtenby', 'uv', 'dv']
    search_fields = ['text', 'id']


@admin.register(Bookmark)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'plot_point']

@admin.register(Edits)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'request_status']

@admin.register(Choice_Edits)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'choice', 'request_status']

@admin.register(Upvotes)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'plot_point']

@admin.register(Downvotes)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'plot_point']

@admin.register(Choice_Upvotes)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'plot_point', 'choice']

@admin.register(Choice_Downvotes)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'plot_point', 'choice']

