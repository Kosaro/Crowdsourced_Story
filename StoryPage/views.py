from django.shortcuts import render, redirect
from StoryPage.DatabaseHelper import *
from StoryPage.forms import *
from django.contrib import messages


# this is the same render function that was filled with dummy data, but you have to pass a PlotPoint object to it.
def plot_point(request, plot_point_id):
    plot = PlotPoint.objects.get(pk=plot_point_id)
    text = plot.pptext
    choices = get_choices(plot)
    author = plot.writtenby
    votes = plot.uv
    context = {'plot_point': text, 'choices': choices, 'votes': votes, 'author': author,
               'username': 'Jenna the Rogue', 'plot_point_id': plot_point_id,
               'bookmarked': False}
    return render(request, 'plotPoint.html', context)


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
            author = form.cleaned_data['author']
            prevpp = PlotPoint.objects.get(pk=plot_point_id)
            prevpp.isEnd = False
            prevpp.save()
            newplotpoint = PlotPoint(pptext=plotpoint_text, writtenby=author)
            newplotpoint.save()
            newchoice = Choice(text=choice_text, writtenby=author, plotpoint=prevpp, destination=newplotpoint.id)
            newchoice.save()
            upvote(request, newplotpoint, author)
            messages.success(request, "New choice added")
            return redirect(plot_point, plot_point_id)


