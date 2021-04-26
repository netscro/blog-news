from rest_framework import serializers, pagination
from rest_framework.fields import SerializerMethodField

from news.models import Category, Post, Comment


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True
    )

    for_post = serializers.SlugRelatedField(
        slug_field="title",
        read_only=True
    )

    class Meta:
        model = Comment
        fields = '__all__'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostSerializer(serializers.ModelSerializer):

    # counter of comments
    comments_count = SerializerMethodField()

    author = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True
    )

    category = serializers.SlugRelatedField(
            slug_field="name",
            read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
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
              )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # calculate count of comments
    def get_comments_count(self, obj):
        return obj.comments.count()


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
