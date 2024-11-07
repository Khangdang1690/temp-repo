# views.py
from django.shortcuts import render

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

def submit_story(request):
    return render(request, 'story_sub.html')
