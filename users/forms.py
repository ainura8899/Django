from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.db.models.signals import post_save
from django.dispatch import receiver

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

LEVEL = (
        ('junior', 'junior'),
        ('middle', 'middle'),
        ('senior', 'senior'),

    )

class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    level = forms.ChoiceField(choices=LEVEL, required=True)
    salary = forms.IntegerField(required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'gender',
            'phone_number',
            'level',
            'salary'
        )

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

@receiver(post_save, sender=models.CustomUser)
def set_salary(sender, instance, created, **kwargs):
    if created:
        level = instance.level
        if level == 'junior':
            instance.salary = 500
        elif level == 'middle':
            instance.salary = 1000
        elif level == 'senior':
            instance.salary = 3000
        else:
            instance.salary = 0
        instance.save()
