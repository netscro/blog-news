from rest_framework import serializers

from news.models import Category, Post, Comment


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True
    )
    for_news = serializers.SlugRelatedField(
        slug_field="title",
        read_only=True
    )

    class Meta:
        model = Comment
        fields = "__all__"

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True)

    author = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True
    )
    category = serializers.SlugRelatedField(
        slug_field="name",
        read_only=True
    )

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
            'comments',
        )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategorySerializer(serializers.ModelSerializer):

    posts = PostSerializer(many=True)

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
