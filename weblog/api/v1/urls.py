from weblog.views import BlogListApi, BlogDetailApi
from django.urls import path


urlpatterns = [
    path('list/', BlogListApi, name='blog_list_api'),
    path('detail/<int:article_id>', BlogDetailApi, name='blog_detail_api'),
]