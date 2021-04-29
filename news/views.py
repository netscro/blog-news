from django.contrib.auth import logout
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from app.utils import IsAdminUserOrReadOnly
from news.models import Post, Category, Comment
from news.serializers import PostSerializer, \
    CategorySerializer, \
    CommentSerializer


class CategoryViewSet(viewsets.ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    # slug instead of id in single category url
    lookup_field = 'slug'
    permission_classes = (IsAdminUserOrReadOnly,)


class PostViewSet(viewsets.ModelViewSet):

    serializer_class = PostSerializer
    # exclude comments with publish = False
    queryset = Post.objects.prefetch_related(Prefetch(
        'comments', queryset=Comment.objects.filter(publish=True)
    )).filter(publish=True)
    # slug instead of id in single post url
    lookup_field = 'slug'
    permission_classes = (IsAdminUserOrReadOnly,)
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
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('for_post',)


class LoginSwaggerUser(View):
    def get(self, request):
        return redirect(reverse('admin:login'))


class LogOutUser(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(
            request.META.get('HTTP_REFERER', reverse('home'))
        )
