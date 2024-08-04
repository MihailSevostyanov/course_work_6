from django.core.mail import send_mail

from mailing.models import Mailing


def start():
    """Функция старта рассылки"""
    scheduler = BackgroundScheduler()
    scheduler.add_job(функция_отправки_письма, 'interval', seconds=10)
    scheduler.start()


def send_mailing(pytz=None):
    """Основная функция по отправке рассылки"""
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    # создание объекта с применением фильтра
    mailings = Модель_рассылки.objects.filter(дата__lte=current_datetime).filter(
        статус_рассылки__in=[список_статусов])

    for mailing in mailings:
        send_mail(
                subject=mailing.theme,
                message=text,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email for client in mailing.клиенты.all()]
           )