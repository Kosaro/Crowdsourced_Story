from django.shortcuts import render
from StoryPage.DataBaseHelper import *

# this is the same render function that was filled with dummy data, but you have to pass a PlotPoint object to it.
def plot_point(request, plot_point):
    text = plot_point.pptext
    choices = get_choices(plot_point)
    author = plot_point.writtenby
    votes = plot_point.uv
    context = {'plot_point': text, 'choices': choices, 'votes': votes, 'author': author, 'username': 'Jenna the Rogue'}
    return render(request, 'plotPoint.html', context)


