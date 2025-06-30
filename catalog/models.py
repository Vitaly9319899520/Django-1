from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя', help_text='введите имя')
    description = models.TextField(max_length=150, verbose_name='описание')
    photo = models.ImageField(upload_to='catalog/foto', blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, verbose_name='категория', null=True, blank=True,related_name='products',)  # привязка
    price = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(blank=True, null=True, help_text='Укажите дату создания')
    updated_at = models.DateField(blank=True, null=True, help_text='Укажите дату изменения')

    class Meta:
        verbose_name = 'Продукт'  # отображение информации
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'category']  # сортиовка по...

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(max_length=150)

    class Meta:
        verbose_name = 'Категория'  # отображение информации
        verbose_name_plural = 'Категории'
        ordering = ['name']  # сортиовка по...

    def __str__(self):
        return self.name
