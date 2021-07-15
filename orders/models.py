from django.db import models

from flowers.models import Flower, Good
from .constants import PAYMENT_METHODS, DELIVERY_METHOD


class Order(models.Model):
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS,
                                      verbose_name='Способ оплаты')
    delivery_method = models.CharField(max_length=9, choices=DELIVERY_METHOD,
                                       verbose_name='Способ доставки')
    gift = models.BooleanField(default=False, verbose_name='Подарок')
    phone = models.CharField(max_length=25, verbose_name='Номер телефона')
    delivery_date = models.DateTimeField( verbose_name='Дата доставки')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    comments = models.TextField(verbose_name='Комментарии')
    created_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    paid = models.BooleanField(default=False, verbose_name='Оплачен')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-created_date',)

    def __str__(self):
        return str(self.id)


class FlowerOrder(models.Model):
    order = models.ForeignKey(Order, verbose_name='Заказ',
                              related_name='order', on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, verbose_name='Цветок',
                               related_name='flower', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    total = models.PositiveIntegerField(verbose_name='Итого')

    def __str__(self):
        return f'{self.flower} / {self.price}'


class GoodsOrder(models.Model):
    order = models.ForeignKey(Order, verbose_name='Заказ',
                              related_name='good_order', on_delete=models.CASCADE)
    good = models.ForeignKey(Good, verbose_name='Товар',
                             related_name='good', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    total = models.PositiveIntegerField(verbose_name='Итого')


    def __str__(self):
        return f'{self.good} / {self.price}'