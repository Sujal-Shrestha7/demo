from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('blog-details/<str:pk>/', views.blog_details, name='blog-details'),
]