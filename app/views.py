from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth.models import auth
from django.contrib import messages

# Create your views here.
def signup(request):
    form = RegisterForm()
    return render(request, 'all_templates/signup_form.html',{"form":form})

def login(request):
    return render(request,'all_templates/login.html')