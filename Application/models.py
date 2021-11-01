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
    
    
class Course(models.Model):
    name = models.CharField(max_length=40, default='')
    professor = models.ForeignKey(User, on_delete=models.CASCADE)


class Thread(models.Model):
    subject = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Post(models.Model):
    content = RichTextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)


class Notification(models.Model):
    notification_type = models.IntegerField()
    to_user = models.ForeignKey(User, related_name='notification_to', on_delete=models.CASCADE, null=True)
    from_user = models.ForeignKey(User, related_name='notification_from', on_delete=models.CASCADE, null=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
