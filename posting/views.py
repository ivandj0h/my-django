from django.shortcuts import render

# get data from outsite


def index(request):
    return render(request, 'posting/index.html')


def about(request):
    return render(request, 'posting/about.html')
