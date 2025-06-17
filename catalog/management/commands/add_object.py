from django.core.management.base import BaseCommand
from unicodedata import category

from catalog.models import Product,Category

class Command(BaseCommand):
    help = 'Добавляет тестовые продукты в базу данных'

    def handle(self, *args, **kwargs):
        # Пример добавления тестовых продуктов
        category, created = Category.objects.get_or_create(name='Тестовая категория', description='Описание тестовой категории')
        Product.objects.create(name='Тестовый продукт 1', description='Описание продукта', price=100, category=category)
        Product.objects.create(name='Тестовый продукт 2', description='Описание продукта', price=200, category=category)
        self.stdout.write(self.style.SUCCESS('Тестовые продукты добавлены'))