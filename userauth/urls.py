from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),  # User registration URL
    path('login/', views.login_view, name='login'),  # User login URL
]
