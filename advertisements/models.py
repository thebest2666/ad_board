from django.db import models

from users.models import User


class Ad(models.Model):
    """
        Модель объявления
    """

    title = models.CharField(max_length=255, verbose_name='Название товара')
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(blank=True, null=True, verbose_name='Описание товара')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Aвтор')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title


class Review(models.Model):
    """
        Модель отзыва
    """

    text = models.TextField(verbose_name='Текст отзыва')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Aвтор')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='Объявление, под которым оставлен отзыв')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text