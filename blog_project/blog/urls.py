from django.urls import path
from .views import post_list, post_detail, category_detail

urlpatterns = [
    path('', post_list, name="post_list_url"),
    path('posts/<int:pk>/', post_detail, name="post_detail_url"),
    path('categories/<int:pk>/', category_detail, name="category_detail_url")
]