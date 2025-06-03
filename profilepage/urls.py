from django.urls import path, include
from . import views

urlpatterns = [
    path('my_profile/', views.profile_page, name='profile'),
    path('edit/', views.update_profile, name='update_profile'),
    path('<str:username>/', views.public_profile, name='public_profile'),
]