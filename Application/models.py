from django.contrib.auth.models import AbstractUser
from django.db import models

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
