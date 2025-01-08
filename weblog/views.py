from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Article, Category
from .serializers import ArticleSerializer
from rest_framework import status


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def BlogListApi(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def BlogDetailApi(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        article.delete()
        result = {"result" : 'this article has deleted'}
        return Response(result, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

