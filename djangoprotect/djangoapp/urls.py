from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('secret/', views.secret, name = 'blog-secret'),
    path('about/', views.about, name = 'blog-about'),
    
]
