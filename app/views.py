from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
import json
from django.contrib.humanize.templatetags.humanize import naturaltime
from app.models import Room,Message,User
from django.http import HttpResponse, JsonResponse
from .forms import RegisterForm,RoomsForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.db.models import Q

# Create your views here.


def index(request):
    return render(request,'index.html',{})
    
def signup(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    return render(request, 'all_templates/signup_form.html', {"form":form})

def signin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('signin')
    return render(request,'all_templates/signin.html')

def logout(request):
    logout(request)
    return redirect('signin')
    

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)
    
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(message=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def getMessages(request, room):
    room_details = Room.objects.get(name=room) 
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})



def chatroom(request, pk:int):
    other_user = get_object_or_404(User, pk=pk)
    messages = Message.objects.filter(
        Q(receiver=request.user, sender=other_user)
    )
    messages.update(seen=True)
    messages = messages | Message.objects.filter(Q(receiver=other_user, sender=request.user) )
    return render(request, "chatroom1.html", {"other_user": other_user, 'users': User.objects.all(), "user_messages": messages})



def ajax_load_messages(request, pk):
    other_user = get_object_or_404(User, pk=pk)
    messages = Message.objects.filter(seen=False, receiver=request.user)
    
    print("messages")
    message_list = [{
        "sender": message.sender.username,
        "message": message.message,
        "sent": message.sender == request.user,
        "picture": other_user.profile.picture.url,

        "date_created": naturaltime(message.date_created),

    } for message in messages]
    messages.update(seen=True)
    
    if request.method == "POST":
        message = json.loads(request.body)['message']
        
        m = Message.objects.create(receiver=other_user, sender=request.user, message=message)
        message_list.append({
            "sender": request.user.username,
            "username": request.user.username,
            "message": m.message,
            "date_created": naturaltime(m.date_created),

            "picture": request.user.profile.picture.url,
            "sent": True,
        })
    print(message_list)
    return JsonResponse(message_list, safe=False)