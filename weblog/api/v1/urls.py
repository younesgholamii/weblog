from weblog.views import my_api
from django.urls import path


urlpatterns = [
    path('list/', my_api, name='blog_list_api')
]