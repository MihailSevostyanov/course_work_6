from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Message(models.Model):
    title = models.CharField(max_length=150, verbose_name="Тема письма", help_text='Введите тему письма', **NULLABLE)
    body = models.TextField(verbose_name="Текст письма", help_text='Введите текст письма', **NULLABLE)


class MailingSettings(models.Model):
    datetime_send = models.DateTimeField(auto_now_add=True, verbose_name='дата и время первой отправки рассылки',
                                         help_text='введите дату и время первой отправки рассылки')
    periodicity = models.PositiveSmallIntegerField(verbose_name='периодичность (через сколько дней)',
                                                   help_text='введите периодичность', default='1')
    status = models.BooleanField(default=True, verbose_name='статус', help_text='введите статус рассылки (ожидается ('
                                                                                'запущена) или завершена)')
    active = models.BooleanField(default=True, verbose_name='активность', help_text='запущена ли рассылка сейчас')


class Mailing(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название рассылки', help_text='Введите название рассылки',
                             **NULLABLE)
    description = models.TextField(verbose_name='Описание', help_text='Введите описание рассылки', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания',
                                      help_text='Введите дату создания статьи')
    message = models.OneToOneField(Message, on_delete=models.CASCADE, verbose_name='сообщение', **NULLABLE,
                                   related_name='message')
    settings = models.OneToOneField(MailingSettings, on_delete=models.CASCADE, verbose_name='настройки', **NULLABLE,
                                    related_name='settings')

    def __str__(self):
        return f"{self.title} {self.description}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ("created_at",)
