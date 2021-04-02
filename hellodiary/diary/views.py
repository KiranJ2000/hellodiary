import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .decorators import unauntheticated_user

from .forms import CreateUserForm, DiaryForm
from .models import Diary
# Create your views here.


@unauntheticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            context = {'first_name' : username}
            return redirect('home')
        else:
            messages.error(request,'Username or Password not correct')
            return redirect('login_page')

    return render(request, 'login.html')

@unauntheticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Successfully Created!')
            return redirect('login_page')
    context = {'form' : form}

    return render(request, 'register.html', context)

def logout_user(request):
    logout(request)

    return redirect('login_page')

@login_required(login_url='login_page')
def home(request):
    context = {'first_name' : request.user.first_name}

    return render(request, 'home.html', context)

@login_required(login_url='login_page')
def all_entries(request):
    return render(request, 'allentries.html')

@login_required(login_url='login_page')
def analytics(request):
    return render(request, 'analytics.html')

@login_required(login_url='login_page')
def create_diary(request):
    current_user = request.user
    form = DiaryForm()

    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid:
            diary = form.save(commit=False)
            diary.user = current_user
            diary.save()

            return redirect('home')
    

    date = datetime.datetime.now().strftime("%d/%m/%Y")
    day = datetime.datetime.now().strftime("%a")

    full_date = day + '.' +  ' ' + date
    
    context = {'form': form, 'full_date': full_date}
    return render(request, 'create_diary.html', context)

