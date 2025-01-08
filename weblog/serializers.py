from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        




# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(required=False)
#     title = serializers.CharField(max_length=110)
#     text = serializers.CharField()
#     image = serializers.ImageField(required=False)
#     slug = serializers.SlugField(required=False)
#     created_at = serializers.DateTimeField(required=False)
#     updated_at = serializers.DateTimeField(required=False)
#     publisher = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#     categories = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    
#     def create(self, validated_data):
#         article = Article.objects.create(**validated_data)
#         return article

