from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(User):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    LEVEL = (
        ('junior', 'junior'),
        ('middle', 'middle'),
        ('senior', 'senior'),

    )

    phone_number = models.CharField(max_length=14, default='+996')
    age = models.PositiveIntegerField(default=18,
                                      validators=[
                                          MaxValueValidator(99),
                                          MinValueValidator(18),
                                      ])
    gender = models.CharField(max_length=10, choices=GENDER)

    level = models.CharField(max_length=10, choices=LEVEL, default='junior')
    salary = models.PositiveIntegerField(max_length=4)


@receiver(post_save, sender=CustomUser)
def set_salary(sender, instance, created, **kwargs):
    if created:
        print("Сигнал обработан, пользователь создан")

        level = instance.level
        if level == 'junior':
            instance.salary = 500
        elif level == 'middle':
            instance.salary = 1000
        elif level == 'senior':
            instance.salary = 3000
        else:
            instance.salary =0
        instance.save()
