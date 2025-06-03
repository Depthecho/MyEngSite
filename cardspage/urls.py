from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.my_cards, name='my_cards'),
    path('add-cards/', views.add_cards, name='add_cards'),
    path('create-card-from-selection/', views.create_card_from_selection, name='create_card_from_selection'),
    path('edit-card/<int:user_card_id>/', views.edit_card, name='edit_card'),
    path('delete/<int:user_card_id>/', views.delete_card, name='delete_card'),
    path('quiz/', views.quiz_start, name='quiz_start'),
    path('quiz/test/', views.quiz, name='quiz'),
    path('quiz/results/', views.quiz_results, name='quiz_results'),
    ]