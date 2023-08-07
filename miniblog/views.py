from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'miniblog/base.html',{})

def home(request):
    return render(request, 'miniblog/home.html', {})

def logout(request):
    return HttpResponseRedirect('/')

def dashboard(request):
    return render(request, 'miniblog/dashboard.html', {})

def signup(request):
    return render(request, 'miniblog/signup.html', {})

def login(request):
    return render(request, 'miniblog/login.html', {})