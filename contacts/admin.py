from django.contrib import admin
from .models import Contact, Social


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone']


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ['contact', 'name', 'link']