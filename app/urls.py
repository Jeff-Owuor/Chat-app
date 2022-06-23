from django.urls import re_path,path,include
from .views import index,signup,logout,signin,room,checkview,send,getMessages,ajax_load_messages,chatroom



urlpatterns = [
    re_path(r'^$', index , name='home'),
    # path('register/', RegisterView.as_view()),
    # path('login/',LoginView.as_view()),
    # path('user/',UserView.as_view()),
    # path('logout/',LogoutView.as_view()),
    # path('refresh/',RefreshView.as_view()),
    re_path(r'^signup',signup,name='signup'),
    re_path(r'^logout',logout,name='logout'),
    re_path(r'^signin',signin,name='signin'), 
    path('<str:room>/', room, name='room'),
    path('checkview', checkview, name='checkview'),
    path('send', send, name='send'),
    path("<int:pk>/", chatroom, name="chatroom"),
    path('getMessages/<str:room>/', getMessages, name='getMessages'),
    path("ajax/<int:pk>/", ajax_load_messages, name="chatroom-ajax"),   
    
]