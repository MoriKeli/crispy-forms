from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView


class UserLogin(LoginView):
    template_name = 'crispy-app/index.html'