from rest_framework import serializers
from Articles.models import Author,Article

class AuthorSerializer(serializers.ModelSerializer):
    user_name = serializers.StringRelatedField(read_only=True)
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = Author
        fields = '__all__'

class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model= Author
        fields = ['avatar']

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Article
        fields='__all__'
        

