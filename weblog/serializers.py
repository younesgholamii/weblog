from rest_framework import serializers


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=110)
    text = serializers.CharField()
    image = serializers.ImageField()
    slug = serializers.SlugField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
