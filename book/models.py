from django.db import models

# Создание новой таблицы с названием Book
class Book(models.Model):

    GENRE_CHOICES = (
        ('Детектив', 'Детектив'),
        ('Психология', 'Психология'),
        ('Детская литература', 'Детская литература')
    )

    title = models.CharField(max_length=255,
                             verbose_name='enter title', db_index=True, null=True)
    image = models.ImageField(upload_to='book/', db_index=True, null=True)
    description = models.TextField(verbose_name='write description', db_index=True, null=True)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES, db_index=True, null=True)
    url_book = models.URLField(verbose_name='write book url', db_index=True, null=True)
    author = models.TextField(verbose_name='write author name', db_index=True, null=True)
    pages = models.IntegerField(verbose_name='write number of pages', db_index=True, null=True)
    price = models.PositiveIntegerField(verbose_name='write price', db_index=True, null=True)
    # Если вы после миграций забыли указать какое-то поле, то так же создаете его,
    # но в атрибуте нового поля, указываете null=True и заново проводите миграции (PS: даже если вы изменили название поля)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, null=True)


    def __str__(self):
        return f'{self.title} - {self.created_at}'

class ReviewBook(models.Model):
    book_review = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review_book', db_index=True, null=True)
    text_book = models.TextField(db_index=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, null=True)

    def __str__(self):
        return f'{self.text_book} - {self.created_at}'
