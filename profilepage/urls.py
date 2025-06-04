from django.urls import path, include
from . import views

urlpatterns = [
    path('my_profile/', views.profile_page, name='profile'),
    path('edit/', views.update_profile, name='update_profile'),
    path('friends/', views.friends_list, name='friends_list'),
    path('followers/', views.followers_list, name='followers_list'),
    path('friends/send/<str:username>/', views.send_friend_request, name='send_friend_request'),
    path('friends/accept/<int:friendship_id>/', views.accept_friend_request, name='accept_friend_request'),
    path('friends/reject/<int:friendship_id>/', views.reject_friend_request, name='reject_friend_request'),
    path('friends/remove/<str:username>/', views.remove_friend, name='remove_friend'),
    path('<str:username>/', views.public_profile, name='public_profile'),
]