from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=100)
    
   
class Message(models.Model):
    message = models.CharField(max_length=100000)
    date = models.DateTimeField(default=datetime.now,blank=True)
    user = models.CharField(max_length=1000)
    room = models.CharField(max_length=1000)