from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_profile, name='my_profile'),
    path('teacher/', views.teacher_profile, name='teacher_profile'),
]