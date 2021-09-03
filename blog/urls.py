# Add path, funtion to routh to, and the name to be accessed from html files 
# Is used in base.html

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]