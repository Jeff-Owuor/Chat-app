from django.contrib import admin
from app.models import User, Room, Message

# Register your models here.
admin.site.register(User)
admin.site.register(Room)
admin.site.register(Message)