from django.urls import path
from . import views

urlpatterns = [
    path('level-test/', views.take_level_test, name='take_level_test'),

    path('level-test/result/<int:result_id>/', views.level_test_result, name='level_test_result'),
]