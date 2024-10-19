from django.urls import path
from . import views

app_name =  'posts'
urlpatterns = [
    path('create/', views.create_post, name='create_post'),  # URL for creating posts
    path('', views.post_list, name='post_list'),  # URL for listing posts
]
