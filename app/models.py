from django.db import models
from django.contrib.auth.models import AbstractUser,User
from cloudinary.models import CloudinaryField
from datetime import datetime

# Create your models here.

class Users(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Room(models.Model):
    name = models.CharField(max_length=100)
    
    
class Message(models.Model):
    message = models.CharField(max_length=100000)
    date = models.DateTimeField(default=datetime.now,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)