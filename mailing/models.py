from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Message(models.Model):
    title = models.CharField(max_length=150, verbose_name="Тема письма", help_text='Введите тему письма', **NULLABLE)
    body = models.TextField(verbose_name="Текст письма", help_text='Введите текст письма', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class MailingSettings(models.Model):
    DAILY = "Раз в день"
    WEEKLY = "Раз в неделю"
    MONTHLY = "Раз в месяц"

    PERIODICITY_CHOICES = [
        (DAILY, 'Раз в день'),
        (WEEKLY, 'Раз в неделю'),
        (MONTHLY, 'Раз в месяц'),
    ]

    CREATED = 'Создана'
    STARTED = 'Запущена'
    COMPLETED = 'Завершена'

    STATUS_CHOICES = [
        (COMPLETED, "Завершена"),
        (CREATED, "Создана"),
        (STARTED, "Запущена"),
    ]
    start_time = models.DateTimeField(verbose_name='время начала рассылки', **NULLABLE)
    end_time = models.DateTimeField(verbose_name='время окончания рассылки', **NULLABLE)
    datetime_send = models.DateTimeField(auto_now_add=True, verbose_name='дата и время первой отправки рассылки',
                                         help_text='введите дату и время первой отправки рассылки')
    periodicity = models.CharField(max_length=50, choices=PERIODICITY_CHOICES, verbose_name='Периодичность')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name='Статус')
    active = models.BooleanField(default=True, verbose_name='активность', help_text='запущена ли рассылка сейчас')

    def __str__(self):
        return f"{self.title} time:{self.start_time} - {self.end_time}, periodicity: {self.periodicity}, status: {self.status}"

    class Meta:
        verbose_name = "Настройки рассылки"
        verbose_name_plural = "Настройки рассылок"
        ordering = ("datetime_send",)


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


class Client(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя клиента', help_text='Введите имя клиента')
    email = models.EmailField(verbose_name='Email клиента', help_text='Введите email клиента')
    comment = models.TextField(verbose_name='Комментарий', help_text='Введите комментарий')
    is_active = models.BooleanField(default=True, verbose_name='активен')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка', **NULLABLE,
                                related_name='mailing')

    def __str__(self):
        return f"{self.name} {self.email}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Log(models.Model):
    time = models.DateTimeField(verbose_name='дата и время последней попытки', auto_now_add=True)
    status = models.CharField(max_length=30, verbose_name='статус попытки')
    server_response = models.CharField(verbose_name='ответ почтового сервера', **NULLABLE)

    mailing_list = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name='рассылка')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент', **NULLABLE)

    def __str__(self):
        return f'{self.time} {self.status}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'