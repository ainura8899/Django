from django.db import models

# Создание новой таблицы с названием Book
class Book(models.Model):

    title = models.CharField(max_length=255,
                             verbose_name='enter title')
    image = models.ImageField(upload_to='book/',
                              verbose_name='download picture')
    description = models.TextField(verbose_name='write description')
    genre = models.IntegerField(verbose_name='Genre', choices=((1, "Детектив"), (2, "Фантастика"),
                        (3, "Детская литература"), (4, "Психология"), (5, "Кулинария")), null=True)
    url_book = models.URLField(verbose_name='write book url', null=True)
    author = models.TextField(verbose_name='write author name')
    pages = models.IntegerField(verbose_name='write number of pages', null=True)
    price = models.PositiveIntegerField(verbose_name='write price')
    # Если вы после миграций забыли указать какое-то поле, то так же создаете его,
    # но в атрибуте нового поля, указываете null=True и заново проводите миграции (PS: даже если вы изменили название поля)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return f'{self.title} - {self.created_at}'

class ReviewBook(models.Model):
    book_review = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review_book')
    text_book = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text_book} - {self.created_at}'
