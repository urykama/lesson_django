from django.core.management.base import BaseCommand  # , CommandError
from blogapp.models import Category, Post, Tag


class Command(BaseCommand):
    # help = 'Closes the specified poll for voting'
    #
    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        # Выбираем все категории
        categories = Category.objects.all()
        print(categories)
        print(type(categories))
        for item in categories:
            print(item)
            print(item.name)
            print(type(item))
        print('END это моя команда')

        # Выбрать одну категорию
        # category = Category.objects.get(name='Игрушки')
        # print(category)
        # print(type(category))

        # Несколько
        category = Category.objects.filter(name='Игрушки')
        print(category)
        print(type(category))

        # первый пост
        post = Post.objects.first()
        print(post)
        print(type(post))

        # связанные поля
        # ForeignKey
        print('# связанные поля')
        print(post.category)
        print(post.category.name)
        print(type(post.category))
        # ManyToMany
        print(post.tags.all())
        print(post.tags.first())
        print(post.tags.first().name)
        print(type(post.tags.first()))
        print(post.tags.filter(name='Один'))

        # print(Tag.objects.first().post.all())
        # Создание
        Category.objects.create(name='Новая3', description='Что то')
        # Изменение
        category = Category.objects.get(name='Измененная3')
        category.name = 'Измененная4'
        category.save()
        # Удаление
        # Одну
        category.delete()
        # несколько
        # Category.objects.all().delete()

        # for poll_id in options['poll_id']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)
        #
        #     poll.opened = False
        #     poll.save()
        #
        #     self.stdout.write('Successfully closed poll "%s"' % poll_id)
