from django.db import models

# Создание новой таблицы с названием Movie
class Movie(models.Model):

    GENRE_CHOICES = (
        ('Ужасы', 'Ужасы'),
        ('Комедия', 'Комедия'),
        ('Фантастика', 'Фантастика')
    )

    title = models.CharField(max_length=255,
                             verbose_name='enter title', db_index=True, null=True)
    image = models.ImageField(upload_to='tv_show/', db_index=True, null=True)
    description = models.TextField(verbose_name='write description', db_index=True, null=True)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES, db_index=True, null=True)
    price = models.PositiveIntegerField(verbose_name='write price', db_index=True, null=True)
    # Если вы после миграций забыли указать какое-то поле, то так же создаете его,
    # но в атрибуте нового поля, указываете null=True и заново проводите миграции (PS: даже если вы изменили название поля)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, null=True)


    def __str__(self):
        return f'{self.title} - {self.created_at}'

class ReviewMovie(models.Model):
    movie_review = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='review_movie', db_index=True, null=True)
    text_movie = models.TextField(db_index=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, null=True)

    def __str__(self):
        return f'{self.text_movie} - {self.created_at}'
