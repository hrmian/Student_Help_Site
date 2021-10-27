from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm
from .models import User


@login_required()
def home(request):
    return render(request, 'home.html')


@login_required()
def user_profile(request):
    return render(request, 'profile.html')

def sign_up(request):
    return render(request, 'sign_up.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')