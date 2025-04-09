from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.my_cards, name='my_cards'),
    path('add-cards/', views.add_cards, name='add_cards'),
    path('edit-card/<int:card_id>/', views.edit_card, name='edit_card'),
    path('delete/<int:card_id>/', views.delete_card, name='delete_card'),
    ]