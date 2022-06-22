from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from datetime import datetime

# Create your models here.

class User(AbstractUser):
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
    user = models.CharField(max_length=1000)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)