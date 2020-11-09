from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Xeno',
        'title': 'School lunch',
        'content': 'bruh',
        'date_posted': 'August 27, 2018'
    },

    {
        'author': 'John roblox',
        'title': 'bruh',
        'content': 'i hate school',
        'date_posted': 'August 28, 2018'

    }
]



def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'brandom/home.html', context)