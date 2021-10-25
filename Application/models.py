from django.db import models

# Create your models here.
class user(models.Model):
    firstname = models.CharField(max_length=30, default='')
    lastname = models.CharField(max_length=30, default='')
    email = models.EmailField(max_length=100, default='')
    password = models.CharField(max_length=30, default='')
    role = models.CharField(max_length=10, default='') #admin, professor, student, alumni, 
    
    
class course(models.Model):
    name = models.CharField(max_length=40, default='')
    professor = models.ForeignKey(user, on_delete=models.CASCADE)
