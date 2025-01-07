from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Article, Category
from .serializers import ArticleSerializer
from rest_framework import status

@api_view(['GET', 'POST'])
def BlogListApi(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            categories_id = request.data.get('categories')
            article = serializer.save()
            for category_id in categories_id:
                category = get_object_or_404(Category, id=category_id)
                article.categories.add(category)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def BlogDetailApi(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        article.delete()
        result = {"result" : 'this article has deleted'}
        return Response(result, status=status.HTTP_204_NO_CONTENT)