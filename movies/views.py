from django.shortcuts import render, HttpResponse,loader

# Create your views here.


def index(req):
    context = {
        'movies': ["Wolf of wallstreet", "Avengers", "Dark Knight"]
    }
    return render(req, 'movies/index.html', context)


def about_me(req):
    return render(req, 'movies/about_me.html')
