from weblog.views import BlogListApi
from django.urls import path


urlpatterns = [
    path('list/', BlogListApi, name='blog_list_api')
]