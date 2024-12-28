from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    publisher = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    categories = models.ManyToManyField("Category", verbose_name='categories')
    title = models.CharField(max_length=110, verbose_name='article title')
    text = models.TextField()
    slug = models.SlugField(blank=True, null=True, verbose_name='article slug')
    image = models.ImageField(verbose_name='article image', upload_to='weblog/articles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='updated at')

    def __str__(self):
        return f"Article {self.title}"


class Category(models.Model):
    title = models.CharField(max_length=110)

    def __str__(self):
        return self.title
    

