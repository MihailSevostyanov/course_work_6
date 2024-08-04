from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Mailing(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название рассылки', help_text='Введите название рассылки',
                             **NULLABLE)
    description = models.TextField(verbose_name='Описание', help_text='Введите описание рассылки', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания',
                                      help_text='Введите дату создания статьи')

    def __str__(self):
        return f"{self.title} {self.description}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ("created_at",)
