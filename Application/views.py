from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from .services import subscribe, send_notifications, report_post


@login_required()
def home(request):
    courses = Course.objects.all().order_by('name')
    threads = Thread.objects.all().order_by('-timestamp');
    return render(request, 'home.html', {'courses': courses, 'threads': threads})


@login_required()
def user_profile(request, username):
    user = User.objects.get(username=username)
    profile = UserProfile.objects.get(user__id=user.id)
    return render(request, 'profile.html', {'user': user, 'profile': profile})


@login_required()
def user_settings(request, username):
    user = User.objects.get(username=username)
    profile = UserProfile.objects.get(user__id=user.id)
    # return render(request, 'user_settings.html', {'user': user, 'profile': profile})
    if request.method == 'POST':
        form = EditAccount(request.POST, instance = request.user)
        if form.is_valid():
            user = form.save()
            #UserProfile.objects.create(user=user)
            return render(request, 'user_settings.html', {'user': user, 'profile': profile, 'form': form})
    else:
        form = EditAccount(instance = request.user)
    return render(request, 'user_settings.html', {'user': user, 'profile': profile, 'form': form})

@login_required()
def settings(request, username):
    user = User.objects.get(username=username)
    profile = UserProfile.objects.get(user__id=user.id)
    return render(request, 'settings.html', {'user': user, 'profile': profile})


@login_required()
def discussions(request, course_id):
    threads = Thread.objects.filter(course__id=course_id)
    course = Course.objects.get(id=course_id)
    return render(request, 'discussions.html', {'threads': threads, 'course': course})


@login_required()
def create_thread(request, course_id):
    # if this doesn't exist load error?
    course = Course.objects.get(id=course_id)

    if request.method == 'POST':
        form1 = ThreadForm(request.POST)
        form2 = PostForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            subject = form1.cleaned_data.get('subject')
            content = form2.cleaned_data.get('content')
            new_thread = Thread.objects.create(subject=subject, user=request.user, course=course)
            Post.objects.create(user=request.user, content=content, thread=new_thread)
            subscribe(request.user, new_thread)
            return redirect('discussions', course_id=course_id)
    else:
        form1 = ThreadForm()
        form2 = PostForm()
        return render(request, 'create_thread.html', {'form1': form1, 'form2': form2})


# clean up - split up?
@login_required()
def thread(request, thread_id):
    t = None
    posts = None
    message = ''
    if Thread.objects.filter(id=thread_id).exists():
        t = Thread.objects.get(id=thread_id)
        posts = Post.objects.filter(thread__id=thread_id)
    else:
        message = "Topic does not exist"

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            Post.objects.create(content=content, user=request.user, thread=t)
            send_notifications(request.user, t)

    form = PostForm()
    return render(request, 'thread.html', {'message': message, 'thread': t, 'posts': posts, 'form': form})

@login_required()
def reported(request, post_id):
    p = None
    meessage = ''
    if Post.objects.filter(id=post_id).exists():
        p = Post.objects.get(id=post_id)
        message = "You have reported the post."
        report_post(reportedPost=p, userReporting=request.user, userReported=p.user)
            
    else:
        message = "ERROR: Post does not exist"
    return render(request, 'reported.html', {'message': message})

@login_required()
def reportedMessages(request):
    reports = None
    if User.objects.get(id=request.user.id).role=='Admin':
        reports = Report.objects.all()
    return render(request, 'all_reports.html', {'reports': reports})

@login_required()
def report_closed(request, report_id, verdict):
    if User.objects.get(id=request.user.id).role=='Admin' & Report.object.filter(id=report_id).exists():
        message=None
        if verdict==1:
            Report.objects.filter(id=report_id).reportedPost.objects.delete()
            message = 'Report closed: Post deleted'
        else:
            Report.objects.filter(id=report_id).delete()
            message = 'Report closed: Deletion denied'
    return render(request, 'report_closed.html', {'message': message})


# redirect to thread by clicking on notification
def thread_notification(request, notification_id, thread_id):
    notification = Notification.objects.get(id=notification_id)
    notification.seen = True
    notification.save()
    return redirect('thread', thread_id=thread_id)


# clear individual notification
def clear_notification(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    notification.seen = True
    notification.save()
    return redirect(request.META.get('HTTP_REFERER'))


# clear all unseen notifications
def clear_all_notifications(request):
    notifications = Notification.objects.filter(to_user=request.user)
    for n in notifications:
        n.seen = True
        n.save()

    return redirect(request.META.get('HTTP_REFERER'))


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/sign_up.html', {'form': form})


def forgot_password(request):
    return render(request, 'forgot_password.html', {'form': ForgotPassForm()})
