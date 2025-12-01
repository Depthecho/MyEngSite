from django.urls import path
from . import views

urlpatterns = [
    path('', views.settings_page, name='settings_page'),
    path('language/', views.language_settings, name='language_settings'),
    path('profile/', views.profile_settings, name='profile_settings'),
    path('privacy_and_security/', views.privacy_and_security_settings, name='privacy_and_security_settings'),
    path('notifications/', views.notifications_settings, name='notifications_settings'),
    path('appearance/', views.appearance_settings, name='appearance_settings'),
    path('data_and_storage/', views.data_and_storage_settings, name='data_and_storage_settings'),
    path('help_and_support/', views.help_and_support_settings, name='help_and_support_settings'),
    path('about/', views.about_settings, name='about_settings'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('terms_of_service/', views.terms_of_service, name='terms_of_service'),

    path('toggle-dark-mode/', views.toggle_dark_mode, name='toggle_dark_mode'),
]