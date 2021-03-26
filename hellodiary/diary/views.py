from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def allEntries(request):
    return render(request, 'allentries.html')

def analytics(request):
    return render(request, 'analytics.html')


