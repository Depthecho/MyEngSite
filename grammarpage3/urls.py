from django.urls import path
from . import views

urlpatterns = [
    path('', views.grammar_list, name='grammar_page'),
    path('<str:main_topic_slug>/', views.grammar_main_topic_detail, name='grammar_main_topic_detail'),
    path('<str:main_topic_slug>/<str:sub_topic_slug>/', views.grammar_sub_topic_detail, name='grammar_sub_topic_detail'),
    ]