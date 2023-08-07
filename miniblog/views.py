from django.http import HttpResponseRedirect
from django.shortcuts import render
from miniblog.forms import LoginForm, SignUpForm

# Create your views here.


def index(request):
    return render(request, 'miniblog/base.html', {})


def home(request):
    return render(request, 'miniblog/home.html', {})


def logout(request):
    return HttpResponseRedirect('/')


def dashboard(request):
    return render(request, 'miniblog/dashboard.html', {})


def signup(request):
    form = SignUpForm()
    return render(request, 'miniblog/signup.html', {'form': form})


def login(request):
    form = LoginForm()
    return render(request, 'miniblog/login.html', {'form': form})
