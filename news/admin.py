from django.contrib import admin

from news.models import Category, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'seo_title',
        'seo_description',
        'publish',
    )
    search_fields = (
        'name',
    )

    prepopulated_fields = {'slug': ('name',)}


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
        'publish',
    )
    search_fields = (
        'title',
    )

    prepopulated_fields = {'slug': ('title',)}
    # show Image from Imagefield
    readonly_fields = ('image_display',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'for_news',
        'author',
        'created_at',
    )


admin.site.site_header = 'Blog-News'
