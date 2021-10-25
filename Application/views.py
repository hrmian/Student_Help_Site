from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm


def user_login(request, **kwargs):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.login(request)
            if user:
                print("test")
                login(request, user)
                return redirect("home")
    else:
        form = LoginForm()
    return render(request, "login.html", {'form': form})


@login_required()
def home(request):
    return render(request, 'home.html')
