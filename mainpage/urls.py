from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('send-code/', views.send_code_view, name='send_code'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='mainpage/reset_password.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='mainpage/reset_password_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='mainpage/reset_password_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='mainpage/reset_password_complete.html'), name='password_reset_complete'),

    path('profile/', include('profilepage.urls')),
    path('cards/', include('cardspage.urls')),
]