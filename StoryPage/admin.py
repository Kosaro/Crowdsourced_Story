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

@admin.register(Edit)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'request_status']

@admin.register(Choice_Edit)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'choice', 'request_status']

@admin.register(Upvote)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'plot_point']

@admin.register(Downvote)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'plot_point']

@admin.register(Choice_Upvote)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'plot_point', 'choice']

@admin.register(Choice_Downvote)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'plot_point', 'choice']

@admin.register(RootPlotPoint)
class RootPlotPoint(admin.ModelAdmin):
    list_display = [field.name for field in RootPlotPoint._meta.get_fields()]
