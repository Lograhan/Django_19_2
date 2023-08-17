from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'c_name': 'Продукты', 'c_description': 'описание продукты'},
            {'c_name': 'Запчасти', 'c_description': 'описание запчасти'},
            {'c_name': 'Игрушки', 'c_description': 'описание игрушки'}
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        Category.objects.all().delete()
        Category.objects.bulk_create(category_for_create)
