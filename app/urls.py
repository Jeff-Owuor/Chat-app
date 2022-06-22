from django.urls import re_path,path,include
from app.views import index,RegisterView,LoginView,UserView,LogoutView,RefreshView,signup,logout,signin, room, checkview



urlpatterns = [
    # paths for the room and checking if user is in a room
    re_path(r'^$', index , name='home'),
    path('<str:room>/', room, name = 'room'),
    path('checkview', checkview, name = 'checkview'),
    
    path('register/', RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('user/',UserView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('refresh/',RefreshView.as_view()),
    re_path(r'^signup',signup,name='signup'),
    re_path(r'^logout',logout,name='logout'),
    re_path(r'^signin',signin,name='signin'),    
    
]