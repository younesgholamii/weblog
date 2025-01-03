from django.urls import path
from .views import my_api

app_name = 'blog'
urlpatterns = [
    path('', my_api, name='blog')
]