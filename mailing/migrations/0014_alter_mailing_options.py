# Generated by Django 4.2.2 on 2024-08-07 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0013_alter_log_mailing_list'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailing',
            options={'ordering': ('created_at',), 'permissions': [('can_turn_off_mailing', 'Can turn off mailing (mailing.settings.status = False'), ('can_not_edit_mailing', 'Can not edit mailing')], 'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
    ]