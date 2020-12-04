from StoryPage.models import *
# returns a python dictionary of ALL of the choices for the passed-in plot point, ordered by upvote count.
def get_choices(plot_point):
    choicelist = Choice.objects.all().filter(plotpoint=plot_point).order_by('uv').values('text')
    return choicelist


# creates a new choice, and the following plot point. auto-upvotes for author. returns the new plotpoint object.
def add_choice(prevpp, choice_text, plotpoint_text, author):
    prevpp.isEnd = False
    prevpp.save()
    newplotpoint = PlotPoint(pptext=plotpoint_text, writtenby=author)
    newplotpoint.save()
    newchoice = Choice(text = choice_text, writtenby= author, plotpoint = prevpp, destination=newplotpoint.id)
    newchoice.save()
    upvote(newplotpoint,author)
    return newplotpoint


# adds an upvote between the plot point and the user
def upvote(plot_point, current_user):
    plot_point.uv = plot_point.uv + 1
    newUV = Upvotes(user=current_user, plot_point=plot_point)
    newUV.save()


# same thing but for choices
def choice_upvote(choice, current_user):
    choice.uv = choice.uv + 1
    newUV = Choice_Upvotes(user=current_user, choice=choice)
    newUV.save()


# ditto
def downvote(plot_point, current_user):
    plot_point.dv = plot_point.dv - 1
    newDV = Downvotes(user=current_user, plot_point=plot_point)
    newDV.save()


def choice_downvote(choice, current_user):
    choice.dv = choice.dv + 1
    newDV = Choice_Downvotes(user=current_user, choice=choice)
    newDV.save()


# favorite but i called it bookmark in the db
def bookmark(plot_point, current_user):
    newbookmark = Bookmark(user=current_user, plot_point=plot_point)
    newbookmark.save()
