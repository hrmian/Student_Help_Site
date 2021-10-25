from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .forms import LoginForm, NewUserForm


class Login(View):
    def get(self, request):
        return render(request, "login.html", {'form': LoginForm()})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.login(request)
            if user:
                request.session["username"] = user.username
                return redirect("home")
        return render(request, "login.html", {'form': form})


class Home(View):
    def get(self, request):
        return render(request, "home.html")

    def post(self, request):
        pass


def CreateAccount(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'createAccount.html', {'form': form})