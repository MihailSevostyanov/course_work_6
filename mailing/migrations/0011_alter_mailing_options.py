# Generated by Django 4.2.2 on 2024-08-07 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0010_mailingsettings_status_changed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailing',
            options={'ordering': ('created_at',), 'permissions': [('can_turn_off_mailing', 'Can turn off mailing (mailing.settings.status = False')], 'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
    ]
