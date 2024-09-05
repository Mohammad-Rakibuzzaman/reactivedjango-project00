# Generated by Django 5.1 on 2024-09-05 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0006_alter_character_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='demo.book'),
        ),
    ]
