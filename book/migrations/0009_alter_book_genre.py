# Generated by Django 5.1.1 on 2024-09-17 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_alter_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('Детектив', 'Детектив'), ('Анимэ', 'Анимэ')], max_length=100, null=True),
        ),
    ]
