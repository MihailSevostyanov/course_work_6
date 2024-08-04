from django.db import models

class Message(models.Model):
    title = models.CharField(max_length=150, verbose_name='Тема сообщения', help_text='Введите тему сообщения')
    body = models.TextField(verbose_name='Сообщение', help_text='Введите сообщение')

