# Generated by Django 5.0.7 on 2024-08-04 19:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0003_mailing'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_send', models.DateTimeField(auto_now_add=True, help_text='введите дату и время первой отправки рассылки', verbose_name='дата и время первой отправки рассылки')),
                ('periodicity', models.PositiveSmallIntegerField(default='1', help_text='введите периодичность', verbose_name='периодичность (через сколько дней)')),
                ('status', models.BooleanField(default=True, help_text='введите статус рассылки (ожидается (запущена) или завершена)', verbose_name='статус')),
                ('active', models.BooleanField(default=True, help_text='запущена ли рассылка сейчас', verbose_name='активность')),
            ],
        ),
        migrations.AlterModelOptions(
            name='message',
            options={},
        ),
        migrations.AddField(
            model_name='mailing',
            name='message',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message', to='mailing.message', verbose_name='сообщение'),
        ),
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.TextField(blank=True, help_text='Введите текст письма', null=True, verbose_name='Текст письма'),
        ),
        migrations.AlterField(
            model_name='message',
            name='title',
            field=models.CharField(blank=True, help_text='Введите тему письма', max_length=150, null=True, verbose_name='Тема письма'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='settings',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='mailing.mailingsettings', verbose_name='настройки'),
        ),
    ]
