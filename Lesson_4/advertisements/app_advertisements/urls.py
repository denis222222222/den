from django.urls import path
from .views import index
from .views import home

urlpatterns = [
    path('', index)
]

urlpatterns = [
    path('', home)
]