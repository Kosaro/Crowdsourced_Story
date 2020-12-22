from django.http import HttpResponse
from django.shortcuts import render, redirect
from StoryPage.DatabaseHelper import *
from StoryPage.forms import *
from StoryPage.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# this is the same render function that was filled with dummy data, but you have to pass a PlotPoint object to it.
def plot_point(request, plot_point_id):
    plot = PlotPoint.objects.get(pk=plot_point_id)
    user = request.user
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
               'username': user, 'plot_point_id': plot_point_id,
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
    username=request.user
    posts = PlotPoint.objects.filter(writtenby=username).values('pptext', 'uv')
    votes_cast = Upvotes.objects.filter(user=username).count()
    posts = [(f['pptext'], f['uv']) for f in posts]
    total_upvotes = 0
    num_posts=0
    for _, votes in posts:
        total_upvotes += int(votes)
        num_posts += 1
    favorites = Bookmark.objects.filter(user=username).values('plot_point__pptext', 'plot_point__writtenby')
    favorites = [(f['plot_point__pptext'], f['plot_point__writtenby']) for f in favorites]

    context = {'posts': posts, 'username': username, 'favorites': favorites, 'votes_cast': votes_cast,
               'total_upvotes':total_upvotes, 'num_posts': num_posts}
    return render(request, 'profile.html', context)

def log_in(request):
    return render(request, 'registration/../templates/login.html')

def sign_up(request):
    return render(request, 'signUp.html')


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
            author = request.user
            prevpp.isEnd = False
            prevpp.save()
            newplotpoint = PlotPoint(pptext=plotpoint_text, writtenby=author_name)
            newplotpoint.save()
            newchoice = Choice(text=choice_text, writtenby=author, plotpoint=prevpp, destination=newplotpoint)
            newchoice.save()
            messages.success(request, "New choice added")
    plot_point_id = form.cleaned_data['plot_point_id']
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
            current_user = request.user.username
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
            plot.uv += 1
            plot.save()
            current_user = request.user
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
            plot.uv -= 1
            plot.save()
            current_user = request.user
            try:
                vote = Downvotes.objects.get(user=current_user, plot_point=plot)
                vote.delete()
            except Downvotes.DoesNotExist:
                newvote = Downvotes(user=current_user, plot_point=plot)
                newvote.save()
            return HttpResponse('Toggled bookmark')
    return HttpResponse('Failed to toggle bookmark')


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/login")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
                #return redirect(plot_point, 1)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    #form = AuthenticationForm()
    #return render(request = request,
        #template_name="1/",
        #context={"form":form})
        return redirect(log_in)

def sign_up(request):
    return render(request, 'signUp.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            #return render(request = request,
                         #template_name = "1/",
                          #context={"form":form})
            return redirect(plot_point,1)

    form = UserCreationForm
    return redirect(plot_point, 1)
    #return render(request = request,
                  #template_name = "signUp.html",
                  #context={"form":form})