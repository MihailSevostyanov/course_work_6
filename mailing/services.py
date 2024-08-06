import datetime
from smtplib import SMTPException

from django.core.mail import send_mail
from django.utils import timezone

from config import settings
from mailing.models import Mailing, Client, Log, MailingSettings


def sending(mailing_item: Mailing):
    """
    Отправка письма
    """
    print(f"mailing_item={mailing_item}...")

    mail_list = Client.objects.filter(mailing=mailing_item)

    for mail in mail_list:
        try:
            print(f"subject={mail.name}, message={mailing_item.message}, from_email={settings.EMAIL_HOST_USER}, "
                  f"to_email={mail.email}")

            result = send_mail(
                subject=mail.name,
                message=mailing_item.message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[mail.email],
                fail_silently=False,
            )

            log_text = f'Send mail {result}, time={timezone.now()}, mailing={mailing_item.title}, mail={mail.email}'
            log = Log.objects.create(log_text=log_text, mailing=mailing_item)
            log.save()

        except SMTPException as error:
            log_text = f'Send mail: error={error}, time={timezone.now()}, mailing={mailing_item.title}, mail={mail.email}'
            log = Log.objects.create(log_text=log_text, mailing=mailing_item)

class send_mails_all_clients():
    datetime_now = datetime.datetime.now(datetime.timezone.utc)
    for mailing_setting in Client.objects.filter(status=MailingSettings.STARTED):

        if (datetime_now > mailing_setting.start_time) and (datetime_now < mailing_setting.end_time):

            for mailing_client in mailing_setting.client.all():
                mailing_log = Log.objects.filter(
                    client=mailing_client.pk,
                    mailing_list=mailing_setting
                )

                if mailing_log.exosts():
                    last_try_date = mailing_log.order_by('-time').first().time

                    if mailing_setting.periodicity == MailingSettings.DAILY:
                        if (datetime_now - last_try_date).days >= 1:
                            sending(mailing_setting, mailing_client)
                    elif mailing_setting.periodicity == MailingSettings.WEEKLY:
                        if (datetime_now - last_try_date).days >= 7:
                            sending(mailing_setting, mailing_client)
                    elif mailing_setting.periodicity == MailingSettings.MONTHLY:
                        if (datetime_now - last_try_date).days >= 30:
                            sending(mailing_setting, mailing_client)
                    else:
                        sending(mailing_setting, mailing_client)


