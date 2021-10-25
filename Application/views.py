from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User


class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("loginUsername")
        password = request.POST.get("loginPassword")
        error = ""

        if username and password and User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if user.check_password(password):
                request.session["username"] = user.username
                return redirect("home")
        else:
            return render(request, "login.html", {"error": error})


class Home(View):
    def get(self, request):
        return render(request, "home.html")

    def post(self, request):
        pass