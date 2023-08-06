from django.contrib import admin
from django.urls import include, path

from . import views

app_name = "miniblog"
urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("signup/", views.dashboard, name="signup"),
    path("login/", views.dashboard, name="login"),
]
