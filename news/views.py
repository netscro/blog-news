from django.db.models import Prefetch
from django.shortcuts import render
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters

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
    # exclude comments with publish = False
    queryset = Post.objects.prefetch_related(Prefetch(
        'comments', queryset=Comment.objects.filter(publish=True)
    )).filter(publish=True)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    filterset_fields = ('category',)
    search_fields = ('title', 'article',)
    ordering_fields = ('title', 'created_at',)


class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    queryset = Comment.objects.filter(publish=True)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('for_post',)


class TestAPI(View):
    def get(self, request):
        return render(request, 'test_drf_api.html')
