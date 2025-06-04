from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    """
    Модель пользователя
    """

    username = None

    ROLE_CHOICES = (
        ('user', 'Пользователь'),
        ('admin', 'Администратор')
    )

    first_name = models.CharField(max_length=20, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия пользователя')
    phone = PhoneNumberField(blank=True, verbose_name='Телефон для связи')
    email = models.EmailField(unique=True, verbose_name='Электронная почта пользователя')
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default='user', verbose_name='Роль пользователя')
    image = models.ImageField(upload_to='users/avatars', blank=True, null=True, verbose_name='Аватарка пользователя')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email