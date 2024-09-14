# Generated by Django 5.1.1 on 2024-09-14 18:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_book_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_book', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_book', to='book.book')),
            ],
        ),
    ]
