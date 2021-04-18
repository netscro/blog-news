from rest_framework import serializers

from news.models import Category, Post, Comment


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostSerializer(serializers.ModelSerializer):

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
        fields = "__all__"

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


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
