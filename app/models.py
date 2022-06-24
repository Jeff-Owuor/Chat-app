from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField
from datetime import datetime

# Create your models here.

User = get_user_model()

class Room(models.Model):
    name = models.CharField(max_length=100)
    
   
class Message(models.Model): 
    message = models.CharField(max_length=100000)
    date = models.DateTimeField(default=datetime.now,blank=True)
    user = models.CharField(max_length=1000)
    room = models.CharField(max_length=1000)
    
    
        
class UserMessages(models.Model):
    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)
    message = models.CharField(max_length=100000)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ("date_created",)