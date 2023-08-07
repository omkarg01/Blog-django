from django.contrib import admin
from django.urls import include, path

from . import views

app_name = "miniblog"
urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("signup/", views.user_signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("addpost/", views.user_addpost, name="addpost"),
    path("updatepost/<int:id>", views.user_updatepost, name="updatepost"),
    path("deletepost/<int:id>", views.user_deletepost, name="deletepost"),
]
