from django.db import models
from django.contrib.auth.models import AbstractUser
<<<<<<< HEAD
=======
from cloudinary.models import CloudinaryField
>>>>>>> fe15d3824e959fcb6945be803312782f8638de84
from datetime import datetime

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
<<<<<<< HEAD
    
class Room(models.Model):
    name = models.CharField(max_length=1000)
    
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    post_date = models.DateTimeField(default = datetime.now, blank=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    room = models.ForeignKey(Room, on_delete= models.CASCADE)
=======


class Room(models.Model):
    name = models.CharField(max_length=100)
    
    
class Message(models.Model):
    message = models.CharField(max_length=100000)
    date = models.DateTimeField(default=datetime.now,blank=True)
    user = models.CharField(max_length=1000)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
>>>>>>> fe15d3824e959fcb6945be803312782f8638de84
