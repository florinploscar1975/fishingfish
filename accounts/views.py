from django.shortcuts import render
from django.contrib.auth.views import LoginView

# Create your views here.

class LoginViewCustom(LoginView):
    template_name = "accounts/login.html"