from django.contrib import admin

from news.models import Category, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'seo_title',
        'seo_description',
    )
    search_fields = (
        'name',
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'author',
        'slug',
        'seo_title',
        'seo_description',
        'created_at',
    )
    search_fields = (
        'title',
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'for_news',
        'author',
        'created_at',
    )
    # search_fields = (
    #     'name',
    # )
