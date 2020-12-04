from django.shortcuts import render
from StoryPage.DatabaseHelper import *


# this is the same render function that was filled with dummy data, but you have to pass a PlotPoint object to it.
def plot_point(request, plot_point_id):
    plot = PlotPoint.objects.get(pk=plot_point_id)
    text = plot.pptext
    choices = get_choices(plot)
    author = plot.writtenby
    votes = plot.uv
    context = {'plot_point': text, 'choices': choices, 'votes': votes, 'author': author, 'username': 'Jenna the Rogue'}
    return render(request, 'plotPoint.html', context)


def profile(request):
    posts = ['testing testing, this is a really long . What happens if I make it so long that it goes on to the next line? '
             'I guess that what we\'re about to find out. post that i want to test', 'post two', 'post 3']
    favorites = ['posts', 'post2']
    username = 'Ella'
    context = {'posts': posts, 'username': username, 'favorites': favorites}
    return render(request, 'profile.html', context)
