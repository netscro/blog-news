from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from news.models import Category, Post, Comment


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True
    )

    class Meta:
        model = Comment
        exclude = ('for_news',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # exclude comments where publish = False
    def to_representation(self, instance):
        comment = super().to_representation(instance)
        if comment['publish']:
            return comment


# serializer for category with exclude fields
class PostSerializerForCategory(serializers.ModelSerializer):
    # counter of comments
    comments_count = SerializerMethodField()

    author = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True
    )

    class Meta:
        model = Post
        fields = (
            'title',
            'slug',
            'article',
            'created_at',
            'author',
            'image',
            'comments_count',
        )

    # calculate count of comments
    def get_comments_count(self, obj):
        return obj.comments.count()


class PostSerializer(PostSerializerForCategory, serializers.ModelSerializer,):
    # related comments to post
    comments = CommentSerializer(many=True)
    category = serializers.SlugRelatedField(
            slug_field="name",
            read_only=True)

    class Meta:
        model = Post
        fields = (
            'title',
            'slug',
            'article',
            'created_at',
            'category',
            'author',
            'image',
            'publish',
            'seo_title',
            'seo_description',
            'comments_count',
            'comments',
             )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategorySerializer(serializers.ModelSerializer):

    # posts = PostSerializer(many=True)
    posts = PostSerializerForCategory(many=True)

    class Meta:
        model = Category
        fields = (
            'name',
            'slug',
            'publish',
            'seo_title',
            'seo_description',
            'posts',
        )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
