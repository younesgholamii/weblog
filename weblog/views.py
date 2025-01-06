from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import status

@api_view(['GET'])
def BlogListApi(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

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