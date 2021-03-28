from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .decorators import unauntheticated_user

from .forms import CreateUserForm
# Create your views here.

@unauntheticated_user
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

@unauntheticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginPage')
    context = {'form' : form}

    return render(request, 'register.html', context)

def logoutUser(request):
    logout(request)

    return redirect('loginPage')

@login_required(login_url='loginPage')
def home(request):
    context = {'first_name' : request.user.first_name}

    return render(request, 'home.html', context)

@login_required(login_url='loginPage')
def allEntries(request):
    return render(request, 'allentries.html')

@login_required(login_url='loginPage')
def analytics(request):
    return render(request, 'analytics.html')


