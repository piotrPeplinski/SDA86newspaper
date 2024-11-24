from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'text', 'date', 'author')


class UserSerializer(serializers.ModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Article.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'articles')
        extra_kwargs = {'password': {
            'write_only': True
        }}

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')

        user = User.objects.create_user(username=username, password=password)
        return user
