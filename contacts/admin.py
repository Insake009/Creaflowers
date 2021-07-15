from django.contrib import admin
from .models import Contact, Social


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone']


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ['contact', 'name', 'link']

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['title']
#
# @admin.register(Flower)
# class FlowerAdmin(admin.ModelAdmin):
#     list_display = ['name', 'price', 'size', 'get_image']
#
#     def get_image(self, obj):
#         return mark_safe(f'<img src={obj.image.url} width="50" height="60"')
#
#     get_image.short_description = 'Изображение'