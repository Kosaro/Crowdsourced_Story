from django.http import HttpResponse
from django.shortcuts import render, redirect
from StoryPage.DatabaseHelper import *
from StoryPage.forms import *
from StoryPage.models import *
from django.contrib import messages


# this is the same render function that was filled with dummy data, but you have to pass a PlotPoint object to it.
def plot_point(request, plot_point_id):
    plot = PlotPoint.objects.get(pk=plot_point_id)
    user = User.objects.get(username="Jenna")
    try:
        Bookmark.objects.get(user=user,plot_point=plot_point_id)
        bookmark = 1
    except:
        bookmark = 0
    try:
        Upvotes.objects.get(user=user,plot_point=plot_point_id)
        upvoted = 1
    except:
        upvoted = 0
    try:
        Downvotes.objects.get(user=user,plot_point=plot_point_id)
        downvoted = 1
    except:
        downvoted = 0
    text = plot.pptext
    choices = get_choices(plot)
    author = plot.writtenby
    votes = plot.uv
    context = {'plot_point': text, 'choices': choices, 'votes': votes, 'author': author,
               'username': 'Jenna', 'plot_point_id': plot_point_id,
               'bookmarked': bookmark,
               'upvoted': upvoted,
               'downvoted': downvoted}
    return render(request, 'plotPoint.html', context)

def open_plot_point(request, form_class=OpenPlotPointForm):
    print(request.method)
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            destination_id = form.cleaned_data['destination_id']
            return redirect(plot_point, destination_id)



def profile(request):
    posts = [
        'testing testing, this is a really long . What happens if I make it so long that it goes on to the next line? '
        'I guess that what we\'re about to find out. post that i want to test', 'post two', 'post 3']
    favorites = ['posts', 'post2']
    username = 'Ella'
    context = {'posts': posts, 'username': username, 'favorites': favorites}
    return render(request, 'profile.html', context)




# creates a new choice, and the following plot point. auto-upvotes for author. returns the new plotpoint object.

def add_choice(request, form_class=NewChoiceForm):
    print(request.method)
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            plot_point_id = form.cleaned_data['plot_point_id']
            choice_text = form.cleaned_data['choice_text']
            plotpoint_text = form.cleaned_data['plot_point_text']
            author_name = form.cleaned_data['author']
            prevpp = PlotPoint.objects.get(pk=plot_point_id)
            author = User.objects.get(username=author_name)
            prevpp.isEnd = False
            prevpp.save()
            newplotpoint = PlotPoint(pptext=plotpoint_text, writtenby=author_name)
            newplotpoint.save()
            newchoice = Choice(text=choice_text, writtenby=author, plotpoint=prevpp, destination=newplotpoint)
            newchoice.save()
            #upvote(request, newplotpoint, author)
            messages.success(request, "New choice added")
            return redirect(plot_point, plot_point_id)


# favorite but i called it bookmark in the db
def toggle_bookmark(request, form_class=ToggleBookmarkForm):
    print(request.method)
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            plot_point_id = form.cleaned_data['plot_point_id']
            user = form.cleaned_data['user']
            plot = PlotPoint.objects.get(pk=plot_point_id)
            current_user = User.objects.get(username=user)
            try:
                bookmark = Bookmark.objects.get(user=current_user, plot_point=plot)
                bookmark.delete()
            except Bookmark.DoesNotExist:
                newbookmark = Bookmark(user=current_user, plot_point=plot)
                newbookmark.save()
            return HttpResponse('Toggled bookmark')
    return HttpResponse('Failed to toggle bookmark')

def toggle_upvote(request, form_class=ToggleUpvoteForm):
    print(request.method)
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            plot_point_id = form.cleaned_data['plot_point_id']
            user = form.cleaned_data['user']
            plot = PlotPoint.objects.get(pk=plot_point_id)
            current_user = User.objects.get(username=user)
            try:
                vote = Upvotes.objects.get(user=current_user, plot_point=plot)
                vote.delete()
            except Upvotes.DoesNotExist:
                newvote = Upvotes(user=current_user, plot_point=plot)
                newvote.save()
            return HttpResponse('Toggled bookmark')
    return HttpResponse('Failed to toggle bookmark')

def toggle_downvote(request, form_class=ToggleDownvoteForm):
    print(request.method)
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            plot_point_id = form.cleaned_data['plot_point_id']
            user = form.cleaned_data['user']
            plot = PlotPoint.objects.get(pk=plot_point_id)
            current_user = User.objects.get(username=user)
            try:
                vote = Downvotes.objects.get(user=current_user, plot_point=plot)
                vote.delete()
            except Downvotes.DoesNotExist:
                newvote = Downvotes(user=current_user, plot_point=plot)
                newvote.save()
            return HttpResponse('Toggled bookmark')
    return HttpResponse('Failed to toggle bookmark')

