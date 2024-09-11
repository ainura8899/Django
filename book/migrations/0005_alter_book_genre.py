# Generated by Django 5.1.1 on 2024-09-11 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_remove_book_created_at_book_pages_book_url_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.IntegerField(choices=[(1, 'Детектив'), (2, 'Фантастика'), (3, 'Детская литература'), (4, 'Психология'), (5, 'Кулинария')], max_length=100, null=True, verbose_name='Genre'),
        ),
    ]
