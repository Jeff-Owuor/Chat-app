from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import get_authorization_header
from .serializers import UserSerializer
from rest_framework.response import Response
from .forms import RegisterForm,RoomsForm
from .models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .authentication import create_access_token,create_refresh_token,decode_access_token,decode_refresh_token
# Create your views here.


def index(request):
    return render(request,'app/index.html',{})

class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class LoginView(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        if user is None:
            raise(AuthenticationFailed('User not found'))
        
        if not user.check_password(password):
            raise(AuthenticationFailed('Incorrect Password'))
        
        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)
        response = Response()
        response.set_cookie(key='refreshToken',value=refresh_token,httponly=True)
        response.data = {
            'token':access_token,
             
        }
        
        return response
            
class UserView(APIView):
    def get(self,request):
        auth = get_authorization_header(request).split()
        
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)
            
            user = User.objects.filter(pk=id).first()
            return Response(UserSerializer(user).data)
        
        raise(AuthenticationFailed('Unauthenticated!'))

class RefreshView(APIView):
    def post(self,request):
        refresh_token = request.COOKIES.get('refreshToken')
        id = decode_refresh_token(refresh_token)
        access_token = create_access_token(id)
        return Response({
            'token':access_token
        })
        
class LogoutView(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie(key='refreshToken')
        response.data = {
            'message':'success'
        }
        return response
    
    
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
    

def room(request,room_id):
    
    if request.method == 'POST':
        form = RoomsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    
    return(request,'all_templates/room.html',{"form":form})