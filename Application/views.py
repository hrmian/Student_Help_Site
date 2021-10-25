from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .forms import LoginForm


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