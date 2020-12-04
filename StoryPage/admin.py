from django.contrib import admin
from StoryPage.models import PlotPoint, Choice, User, Bookmark, Edits, Choice_Edits
from StoryPage.models import Upvotes, Downvotes, Choice_Upvotes, Choice_Downvotes


@admin.register(PlotPoint)
class PlotPointAdmin(admin.ModelAdmin):
    list_display = ['pptext', 'writtenby', 'uv', 'dv']
    search_fields = ['pptext', 'id']


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['text', 'writtenby', 'uv', 'dv']
    search_fields = ['text', 'id']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    search_fields = ['username']

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
