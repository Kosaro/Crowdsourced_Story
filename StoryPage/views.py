from django.shortcuts import render
from django.http import HttpResponse

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
    choices = list(range(20))
    context = {'plot_point': text, 'choices': choices}
    return render(request, 'plotPoint.html', context)
