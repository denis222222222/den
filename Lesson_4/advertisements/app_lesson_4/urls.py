from django.urls import path
from . import views

urlpatterns = [
path('lesson-4/', views.lesson_4, name='lesson_4'),
]