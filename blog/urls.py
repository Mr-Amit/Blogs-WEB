# Add path, funtion to routh to, and the name to be accessed from html files 
# Is used in base.html

from django.urls import path
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
]