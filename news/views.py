from django.shortcuts import render
from django.views import View
from rest_framework import viewsets, permissions

from news.models import Post, Category, Comment
from news.serializers import PostSerializer, \
    CategorySerializer, \
    CommentSerializer


class CategoryViewSet(viewsets.ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PostViewSet(viewsets.ModelViewSet):

    serializer_class = PostSerializer
    queryset = Post.objects.filter(publish=True)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    queryset = Comment.objects.filter(publish=True)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class TestAPI(View):
    def get(self, request):
        return render(request, 'test_drf_api.html')
