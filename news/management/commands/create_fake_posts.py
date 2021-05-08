from django.contrib.auth.models import User
from django.core.management import BaseCommand
from faker import Faker
from random import choice

from news.models import Category, Post, Comment


class Command(BaseCommand):

    help = 'Add new posts, categories and comments in to the database. '

    def add_arguments(self, parser):
        """
        The number of default posts and comments added in to the database
        """
        parser.add_argument('-l', '--len', type=int, default=20)

    def handle(self, *args, **options):

        faker = Faker()

        # Create categories
        if Category.objects.all().count() == 0:
            Category.objects.bulk_create(
                [
                    Category(
                            name='Politics',
                            slug='politics',
                            seo_title='Politics - read online on Blog-News',
                            seo_description='Last news of Politics '
                                            'from all world. '
                                            'Read online on Blog-News.'
                    ),
                    Category(
                            name='Finance',
                            slug='finance',
                            seo_title='Finance - read online on Blog-News',
                            seo_description='Last news of Finance '
                                            'from all world. '
                                            'Read online on Blog-News.'
                    ),
                    Category(
                            name='Economics',
                            slug='economics',
                            seo_title='Economics - read online on Blog-News',
                            seo_description='Last news of Economics '
                                            'from all world. '
                                            'Read online on Blog-News.'
                    ),
                    Category(
                            name='Sports',
                            slug='sports',
                            seo_title='Sports - read online on Blog-News',
                            seo_description='Last news of Sports '
                                            'from all world. '
                                            'Read online on Blog-News.'
                    )
                ]
            )

        all_categories = Category.objects.all()
        list_category_name = [category.name for category in all_categories]

        all_users_is_staff = User.objects.all()
        list_all_users_is_staff = [user.username for user in
                                   all_users_is_staff if user.is_staff]

        for new_post in range(options['len']):
            post = Post()
            post.title = faker.sentence(
                nb_words=5,
                variable_nb_words=False).replace('.', '')

            post.slug = f'{post.title}'.lower().replace(' ', '-').replace('.', '')  # noqa
            post.article = faker.text()
            # random Category
            post.category = Category.objects.get(
                name=choice(list_category_name)
            )
            # random user is_staff
            post.author = User.objects.get(
                username=choice(list_all_users_is_staff)
            )
            post.seo_title = f'{post.title} | ' \
                             f'Read online | Blog news'.replace('.', '')
            post.seo_description = f'{post.title} | Blog news.'
            post.save()

            # list for random posts
            all_posts = Post.objects.all()
            list_post_name = [post.id for post in all_posts]
            # create comments
            comment = Comment()
            comment.text = faker.text()
            # random Post
            comment.for_post = Post.objects.get(
                id=choice(list_post_name)
            )
            # random user is_staff
            comment.author = User.objects.get(
                username=choice(list_all_users_is_staff)
            )
            comment.save()
