from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, ForgotPassForm, SignUpForm, ReplyForm, TopicForm
from .models import User, Topic, Reply, Course


@login_required()
def home(request):
    courses = Course.objects.all()
    return render(request, 'home.html', {'courses': courses})


@login_required()
def user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'profile.html', {'user': user})


@login_required()
def discussions(request, course_id):
    topics = Topic.objects.filter(course__id=course_id)
    return render(request, 'discussions.html', {'topics': topics, 'id': course_id})


@login_required()
def create_topic(request, course_id):
    # if this doesn't exist load error
    course = Course.objects.get(id=course_id)

    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            content = form.cleaned_data.get('content')
            Topic.objects.create(subject=subject, content=content, user=request.user, course=course)
            return redirect('discussions', course_id=course_id)
    else:
        form = TopicForm()
        return render(request, 'create_topic.html', {'form': form})


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


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': SignUpForm()})


def forgot_password(request):
    return render(request, 'forgot_password.html', {'form': ForgotPassForm()})
