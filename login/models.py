from django.db import models

# Create your models here.
class User_Info(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    des = models.TextField()
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    email = models.EmailField()
    dob = models.DateField()
    joined = models.DateTimeField(null=True)

class Friend(models.Model):
    left_user = models.CharField(max_length = 30)
    right_user = models.CharField(max_length = 30)

class Time_Data(models.Model):
    username = models.CharField(max_length = 15)
    duration = models.DateTimeField(null=True)
    end_duration = models.DateTimeField(null=True ,blank=True)