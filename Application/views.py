from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm
from .models import User, Topic, Reply


@login_required()
def home(request):
    return render(request, 'home.html')


@login_required()
def user_profile(request):
    return render(request, 'profile.html')


@login_required()
def discussions(request):
    topics = Topic.objects.all()
    return render(request, 'discussions.html', {'topics': topics})


@login_required()
def topic(request, discussion_topic):
    t = None
    replies = None
    message = ''
    if Topic.objects.filter(id=discussion_topic).exists():
        t = Topic.objects.get(id=discussion_topic)
        replies = Reply.objects.filter(topic__id=discussion_topic)
    else:
        message = "Topic does not exist"
    return render(request, 'topic.html', {'message': message, 'topic': t, 'replies': replies})
