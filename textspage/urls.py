from django.urls import path
from . import views

urlpatterns = [
    path('', views.texts_page, name='texts_page'),
    path('<int:pk>/', views.text_detail, name='text_detail'),
    ]