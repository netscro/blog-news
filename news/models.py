from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.fields import AutoSlugField


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from='name',
                         max_length=100,
                         unique=True,
                         verbose_name='URL')

    seo_title = models.CharField(max_length=100, unique=True, null=True)
    seo_description = models.CharField(max_length=180, unique=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    article = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='title',
                         max_length=200,
                         unique=True,
                         verbose_name='URL')
    image = models.ImageField(upload_to='pictures', null=True, blank=True)

    seo_title = models.CharField(max_length=100, unique=True, null=True)
    seo_description = models.CharField(max_length=180, unique=True, blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']

    def __str__(self):
        date_only = self.created_at.strftime("%d:%M-%Y")
        return f'{self.title} - {date_only}'


class Comment(models.Model):
    text = models.TextField(max_length=500, null=True)
    for_news = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-created_at']

    def __str__(self):
        date_only = self.created_at.strftime("%d:%M-%Y")
        return f'{self.for_news} - {date_only}'

