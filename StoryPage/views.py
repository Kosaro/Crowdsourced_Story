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
