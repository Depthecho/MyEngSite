from django.urls import path
from . import views

app_name = 'messenger'

urlpatterns = [
    path('', views.chat_list, name='chat_list'),
    path('chat/<int:chat_id>/', views.chat_detail, name='chat_detail'),
    path('start/<int:user_id>/', views.start_chat, name='start_chat'),
    path('send_message/<int:chat_id>/', views.send_message, name='send_message'),
    path('create/', views.select_friend_for_chat, name='select_friend_for_chat'),
    path('select_friend/', views.select_friend_for_chat, name='select_friend_for_chat'),
]