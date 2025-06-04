from django.urls import path
from . import views

app_name = 'friendship'

urlpatterns = [
    path('send/<str:username>/', views.send_friend_request, name='send'),
    path('accept/<int:friendship_id>/', views.accept_friend_request, name='accept'),
    path('reject/<int:friendship_id>/', views.reject_friend_request, name='reject'),
    path('remove/<str:username>/', views.remove_friend, name='remove'),
]