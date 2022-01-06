from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class URL(models.Model):
    shorted_url = models.SlugField(max_length=8, unique=True, verbose_name='Сокращенная ссылка', db_index=True)
    full_url = models.URLField(verbose_name='Полная ссылка')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Кто создал?')

    def __str__(self):
        return self.shorted_url

    def get_absolute_url(self):
        return reverse('redirect_original', kwargs={'url_slug': self.shorted_url})

    class Meta:
        verbose_name = 'Сокращенные ссылки'
        verbose_name_plural = 'Сокращенные ссылки'
        ordering = ['create_date']
