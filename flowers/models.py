from django.db import models
from .constants import *

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

class Flower(models.Model):
    category = models.ManyToManyField(Category, related_name='flowers',
                                      verbose_name='Категория')
    name = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(upload_to='flowers', verbose_name='Фото')
    old_price = models.DecimalField(max_digits=8, decimal_places=2,
                                    verbose_name='Старая цена',blank=True,null=True)
    price = models.DecimalField(max_digits=8,decimal_places=2,verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    size = models.CharField(choices=SIZES, max_length=9,verbose_name='Размер')
    date_created = models.DateTimeField(auto_now=True,verbose_name='Время создания')


    class Meta:
        verbose_name = 'Цветок'
        verbose_name_plural = 'Цветы'

    def __str__(self):
        return f'{self.name} / {self.price}'

class Good(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    old_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Старая цена', blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='goods', verbose_name='Фото')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name} / {self.price}'
