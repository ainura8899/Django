# Generated by Django 5.1.1 on 2024-09-10 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[(1, 'Детектив'), (2, 'Фантастика'), (3, 'Детская литература'), (4, 'Психология'), (4, 'Кулинария')], max_length=100, null=True),
        ),
    ]
