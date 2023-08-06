from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'miniblog/base.html',{})

def home(request):
    return render(request, 'miniblog/home.html', {})

def logout(request):
    # return render(request, 'miniblog/lo.html', {})
    pass

def signup(request):
    return render(request, 'miniblog/signup.html', {})

def login(request):
    return render(request, 'miniblog/login.html', {})