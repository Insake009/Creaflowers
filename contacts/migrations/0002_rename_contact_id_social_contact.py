# Generated by Django 3.2.2 on 2021-05-12 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='social',
            old_name='contact_id',
            new_name='contact',
        ),
    ]