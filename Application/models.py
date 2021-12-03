from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField

ROLES = (
    ('Admin', 'Admin'),
    ('Professor', 'Professor'),
    ('Student', 'Student'),
    ('Alum', 'Alum')
)


class User(AbstractUser):
    role = models.CharField(max_length=20, choices=ROLES, default='Student')


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile',
                                on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000, blank=True, null=True)
    major = models.TextField(max_length=30, blank=True, null=True)
    image = models.ImageField(default='static/images/default_profile.svg', blank=True)


class Course(models.Model):
    name = models.CharField(max_length=40, default='')
    professor = models.ForeignKey(User, on_delete=models.CASCADE)


class Thread(models.Model):
    subject = models.CharField(max_length=40)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Post(models.Model):
    content = RichTextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)


class Notification(models.Model):
    # 1 = post in your thread, 2 = post has been flagged/hidden, 3 =
    notification_type = models.IntegerField()
    to_user = models.ForeignKey(User, related_name='notification_to', on_delete=models.CASCADE, null=True)
    from_user = models.ForeignKey(User, related_name='notification_from', on_delete=models.CASCADE, null=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)

class Report(models.Model):
    userReporting = models.ForeignKey(User, related_name='user_reporting', on_delete=models.CASCADE)
    userReported = models.ForeignKey(User, related_name='user_reported', on_delete=models.CASCADE)
    reportedPost = models.ForeignKey(Post, on_delete=models.CASCADE)