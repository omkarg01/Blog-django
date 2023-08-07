from django.http import HttpResponseRedirect
from django.shortcuts import render
from miniblog.forms import LoginForm, SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from miniblog.models import Post

# Create your views here.
def index(request):
    return render(request, 'miniblog/base.html', {})


def home(request):
    posts = Post.objects.all()
    return render(request, 'miniblog/home.html', {'posts': posts})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def dashboard(request):
    posts = Post.objects.all()
    return render(request, 'miniblog/dashboard.html', {'posts': posts})


def user_signup(request):
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


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(request, username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard/')
        else :
            form = LoginForm()
        return render(request, 'miniblog/login.html', {'form': form})
    else: 
        return HttpResponseRedirect('/dashboard/')

def user_addpost(request):
    return render(request, 'miniblog/addpost.html', {})

def user_updatepost(request, id):
    return render(request, 'miniblog/updatepost.html', {})

def user_deletepost(request, id):
    pass

