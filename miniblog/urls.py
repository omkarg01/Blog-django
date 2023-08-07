from django.contrib import admin
from django.urls import include, path

from . import views

app_name = "miniblog"
urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
]
