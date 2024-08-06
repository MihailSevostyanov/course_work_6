from django.contrib import admin

from mailing.models import Mailing, Client, MailingSettings, Message, Log


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'message', 'settings', 'created_at')
    list_filter = ('created_at',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'comment', 'mailing', 'is_active')
    list_filter = ('name',)


@admin.register(MailingSettings)
class MailSettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'datetime_send', 'periodicity', 'status', 'active', 'status_changed')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body')
    list_filter = ('title',)


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'status', 'server_response', 'mailing_list', 'client')
    list_filter = ('time',)
