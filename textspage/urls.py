from django.urls import path
from . import views

urlpatterns = [
    path('', views.texts_page, name='texts_page'),
    path('completed/', views.completed_texts, name='completed_texts'),
    path('<int:pk>/complete/', views.complete_text, name='complete_text'),
    path('<int:pk>/', views.text_detail, name='text_detail'),
    ]