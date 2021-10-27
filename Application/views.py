from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, ReplyForm, TopicForm
from .models import User, Topic, Reply
from datetime import datetime


@login_required()
def home(request):
    return render(request, 'home.html')


@login_required()
def user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'profile.html', {'user': user})


@login_required()
def discussions(request):
    topics = Topic.objects.all()
    return render(request, 'discussions.html', {'topics': topics})


@login_required()
def create_topic(request):
    message = ''
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            content = form.cleaned_data.get('content')
            course = form.cleaned_data.get('course')
            Topic.objects.create(subject=subject, content=content, user=request.user, course=course)
            return redirect('discussions')
    else:
        form = TopicForm()
        return render(request, 'create_topic.html', {'message': message, 'form': form})


# clean up - split up?
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

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            Reply.objects.create(content=content, user=request.user, topic=t)

    form = ReplyForm()
    return render(request, 'topic.html', {'message': message, 'topic': t, 'replies': replies, 'form': form})
