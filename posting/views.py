from django.shortcuts import render

# get data from outsite


def index(request):
    return render(request, 'index.html')
