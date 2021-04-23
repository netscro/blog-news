from django.contrib.auth.models import User
from django.core.management import BaseCommand
from faker import Faker
from random import choice

from news.models import Category, Post, Comment


class Command(BaseCommand):

    help = 'Add new post and comments in to the database. ' \
           'Before run command you must create a superuser with name = admin' \
           'and create base category'

    def add_arguments(self, parser):
        """
        The number of default posts and comments added to the database
        """
        parser.add_argument('-l', '--len', type=int, default=20)

    def handle(self, *args, **options):

        faker = Faker()

        all_posts = Post.objects.all()
        list_post_name = [post.title for post in all_posts]

        all_categories = Category.objects.all()
        list_category_name = [category.title for category in all_categories]

        for new_post in range(options['len']):
            post = Post()
            post.title = faker.sentence(
                nb_words=5,
                variable_nb_words=False).replace('.', '')

            post.slug = f'{post.title}'.lower().replace(' ', '-').replace('.', '')  # noqa
            post.article = faker.text()
            post.category = Category.objects.get(name=choice(list_category_name)) # noqa
            post.author = User.objects.get(username='admin')
            post.seo_title = f'{post.title} | Read online | Blog news'.replace('.', '') # noqa
            post.seo_description = f'{post.article}'
            post.save()

            comment = Comment()
            comment.text = faker.text()
            comment.for_news = Post.objects.get(title=choice(list_post_name))
            comment.author = User.objects.get(username='admin')
            comment.save()
