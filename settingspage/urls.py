from django.urls import path
from . import views

urlpatterns = [
    path('', views.settings_page, name='settings_page'),
    path('language/', views.language_settings, name='language_settings'),
    path('profile/', views.profile_settings, name='profile_settings'),
]