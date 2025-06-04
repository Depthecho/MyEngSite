from django.urls import path, include
from . import views

urlpatterns = [
    path('my_profile/', views.profile_page, name='profile'),
    path('edit/', views.update_profile, name='update_profile'),
    path('friends/', views.friends_list, name='friends_list'),

    path('friendship/', include('profilepage.friendship_urls')),

    path('followers/', views.followers_list, name='followers_list'),
    path('<str:username>/', views.public_profile, name='public_profile'),
    path('notifications/mark_all_as_read/', views.mark_all_notifications_as_read, name='mark_all_as_read'),
    path('notifications/delete/<int:notification_id>/', views.delete_notification, name='delete_notification'),
]