from django.shortcuts import render

def homepage(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')