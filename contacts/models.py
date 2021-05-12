from django.db import models
from .constants import SOCIAL_MEDIA_CHOICES

class Contact(models.Model):
    address = models.CharField(max_length=50, verbose_name='Адрес')
    phone = models.CharField(max_length=25, verbose_name='Номер телефона')
    longitube = models.CharField(max_length=255, verbose_name='Долгота')
    latitube = models.CharField(max_length=255, verbose_name='Широта')

    class Meta:
        verbose_name = verbose_name_plural = 'Контакты'
    def __str__(self):
        return self.phone

class Social(models.Model):
    contact_id = models.ForeignKey(Contact, related_name='links', verbose_name='Контакт', on_delete=models.CASCADE)
    name = models.CharField(choices=SOCIAL_MEDIA_CHOICES,max_length=9,verbose_name='Соц сеть')
    link = models.URLField(verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Соц сеть'
        verbose_name_plural = 'Соц сети'

    def __str__(self):
        return f'{self.contact.phone} at {self.name}'


