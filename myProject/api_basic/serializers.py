from django.db.models import fields
from rest_framework import serializers
from rest_framework import decorators
from .models import Article
from django.contrib.auth.models import User

# class ArticleSerializer(serializers.Serializer):     
#     title = serializers.CharField(max_length=100)
#     author = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=100)
#     date = serializers.DateTimeField()

#     def create(self, validated_data):
#         return Article.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.email = validated_data.get('email', instance.email)
#         instance.date = validated_data.get('date', instance.date)
#         instance.save()
#         return instance

# you can also use ModelSerializer to get rid of extra code
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ['id', 'title', 'author', 'email']
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    article = serializers.HyperlinkedRelatedField(many=True, view_name='article-detail', read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'article', 'owner']
