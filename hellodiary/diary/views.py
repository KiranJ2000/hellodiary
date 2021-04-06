import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.views.generic.detail import DetailView

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
    diary = Diary.objects.filter(user=request.user).order_by('-pk')
    context = {'forms' : diary}

    return render(request, 'allentries.html', context)

@login_required(login_url='login_page')
def analytics(request):
    return render(request, 'analytics.html')

@login_required(login_url='login_page')
def create_diary(request):
    current_user = request.user
    form = DiaryForm()

    date = datetime.datetime.now().strftime("%d/%m/%Y")
    day = datetime.datetime.now().strftime("%a")

    full_date = day + '.' +  ' ' + date

    if request.method == 'POST':

        request.POST._mutable = True
        request.POST['date_created'] = full_date
        request.POST._mutable = False
        form = DiaryForm(request.POST)

        if form.is_valid():
            diary = form.save(commit=False)
            diary.user = current_user
            diary.date_created = full_date
            diary.save()

            return redirect('home')
    
    context = {'form': form, 'full_date': full_date}
    return render(request, 'create_diary.html', context)


@login_required(login_url='login_page')
def detail_view(request, slug, pk):
    try:
        current_object = Diary.objects.get(id=pk)
    except:
        return render(request, 'notfound.html')

    if current_object.user != request.user or not current_object:
        return render(request, 'notfound.html')

    context = {'diary':current_object}
    
    return render(request, 'detailview.html', context)
    



class DiaryDetailedView(DetailView):
    model = Diary
    template_name = 'detailview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context



