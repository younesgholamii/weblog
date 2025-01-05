from django.urls import path
from .views import BlogListApi

app_name = 'blog'
urlpatterns = [
    path('', BlogListApi, name='blog')
]