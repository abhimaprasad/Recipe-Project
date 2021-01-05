from django.contrib import admin
from django.urls import path,include
from users.views import register,Login,Logout
urlpatterns = [
    path("register",register,name="register"),
    path("login",Login,name="login"),
    path("logout",Logout,name="logout"),
    ]