from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


from .forms import CreateUserForm
# Create your views here.

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            context = {'first_name' : username}
            return redirect('home')
        else:
            messages.error(request,request.POST)
            return redirect('loginPage')

    return render(request, 'login.html')

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginPage')
    context = {'form' : form}

    return render(request, 'register.html', context)

def home(request):
    context = {'first_name' : request.user.first_name}
    print(context)
    return render(request, 'home.html', context)

def allEntries(request):
    return render(request, 'allentries.html')

def analytics(request):
    return render(request, 'analytics.html')


