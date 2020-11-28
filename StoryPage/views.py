from django.shortcuts import render


def plot_point(request):
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, ' \
           'sed do eiusmod tempor incididunt ut labore et dolore magna ' \
           'aliqua. Ut enim ad minim veniam, quis nostrud exercitation ' \
           'ullamco laboris nisi ut aliquip ex ea commodo consequat. ' \
           'Duis aute irure dolor in reprehenderit in voluptate velit esse ' \
           'cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat ' \
           'cupidatat non proident, sunt in culpa qui officia deserunt mollit ' \
           'anim id est laborum'
    choices = ['Choice 1', 'Choice 2', 'Choice 3']
    author = 'Ella'
    votes = 0
    context = {'plot_point': text, 'choices': choices, 'votes': votes, 'author': author, 'username': 'Jenna the Rogue'}
    return render(request, 'plotPoint.html', context)


def profile(request):
    posts = ['testing testing, this is a really long . What happens if I make it so long that it goes on to the next line? '
             'I guess that what we\'re about to find out. post that i want to test', 'post two', 'post 3']
    username = 'Ella'
    context = {'posts': posts, 'username': username}
    return render(request, 'profile.html', context)
