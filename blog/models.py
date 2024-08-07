from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок статьи", help_text='Введите заголовок статьи')
    body = models.TextField(verbose_name='Содержимое стати', help_text='Добавьте содержимое статьи')
    image = models.ImageField(upload_to='blog/photo/', verbose_name='Превью', help_text='Загрузите превью статьи', **NULLABLE)
    slug = models.SlugField(unique=True, verbose_name='slug', help_text='slug', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', help_text='Укажите дату создания')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации', help_text='Укажите признак публикации')
    number_views = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров', help_text='Укажите количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
