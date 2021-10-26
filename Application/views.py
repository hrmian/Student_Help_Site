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
