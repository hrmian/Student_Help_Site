from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField

ROLES = (
    ('Admin', 'Admin'),
    ('Professor', 'Professor'),
    ('Student', 'Student'),
    ('Alum', 'Alum')
)


# Create your models here.
class User(AbstractUser):
    role = models.CharField(max_length=20, choices=ROLES, default='Student')
    
    
class Course(models.Model):
    name = models.CharField(max_length=40, default='')
    professor = models.ForeignKey(User, on_delete=models.CASCADE)


class Topic(models.Model):
    subject = models.CharField(max_length=40)
    content = RichTextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Reply(models.Model):
    content = RichTextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
