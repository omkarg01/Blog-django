from django.http import HttpResponseRedirect
from django.shortcuts import render
from miniblog.forms import LoginForm, SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'miniblog/base.html', {})


def home(request):
    return render(request, 'miniblog/home.html', {})


def logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def dashboard(request):
    return render(request, 'miniblog/dashboard.html', {})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'You have successfully signed up!')
            # login(request, user)
            # return HttpResponseRedirect('/')
    else :
        form = SignUpForm()
    return render(request, 'miniblog/signup.html', {'form': form})


def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(request, username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !!')
                    return HttpResponseRedirect('/dashboard/')
        else :
            form = LoginForm()
        return render(request, 'miniblog/login.html', {'form': form})
    else: 
        return HttpResponseRedirect('/dashboard/')
