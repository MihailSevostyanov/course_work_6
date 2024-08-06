from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from mailing.forms import MailingForm, ClientForm, MessageForm, MailingSettingsForm
from mailing.models import Mailing, Client, Message, MailingSettings
from mailing.utils.utils import get_info_and_send, select_mailings


class HomePageView(TemplateView):
    template_name = "mailing/home_page.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = "Главная страница"
        return context_data


"""Контроллеры рассылки"""


class MailingListView(ListView):
    model = Mailing

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        list_mailing = Mailing.objects.all()
        context_data['list_mailing'] = list_mailing
        return context_data


class MailingDetailView(DetailView):
    model = Mailing

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing:mailing_list")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing:mailing_list")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy("mailing:mailing_list")


"""Контроллеры клиентов"""


class ClientListView(ListView):
    model = Client

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        list_clients = Client.objects.all()
        context_data['list_clients'] = list_clients
        return context_data


class ClientDetailView(DetailView):
    model = Client

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("mailing:client_list")


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("mailing:client_list")


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("mailing:client_list")


"""Контроллеры сообщений"""


class MessageListView(ListView):
    model = Message

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        list_messages = Message.objects.all()
        context_data['list_messages'] = list_messages
        return context_data


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailing:message_list")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailing:message_list")


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy("mailing:message_list")


"""Контроллеры ностроек рассылки"""


class MailingSettingsListView(ListView):
    model = MailingSettings

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        list_settings = MailingSettings.objects.all()
        context_data['list_settings'] = list_settings
        return context_data


class MailingSettingsCreateView(DetailView):
    model = MailingSettings
    form_class = MailingSettingsForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data


class MailingSettingsUpdateView(UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy("mailing:settings_list")


class MailingSettingsDeleteView(DeleteView):
    model = MailingSettings
    success_url = reverse_lazy("mailing:settings_list")


def mailing_send(request, pk):
    mailing_item = get_object_or_404(Mailing, pk=pk)

    print(f"mailing_send {mailing_item}")

    try:
        # sending(mailing_item)
        get_info_and_send(mailing_item)
    except Exception as e:
        print("Ошибка")
        print(e)
    else:
        mailing_item.status = True
        mailing_item.save()

    print(mailing_item)
    # print(mailing_item.status)

    select_mailings()

    return redirect(reverse('mailing:mailing_list'))


def toggle_activity_mailing(request, pk):
    mailing_item = get_object_or_404(Mailing, pk=pk)
    if mailing_item.settings.status:
        mailing_item.settings.status = False
    else:
        mailing_item.settings.status = True

    mailing_item.settings.save()

    return redirect(reverse('mailing:mailing_list'))


class HomePageView(TemplateView):
    template_name = "mailing/home_page.html"

    def get_context_data(self, **kwargs):
        """
        - количество рассылок всего,
        - количество активных рассылок,
        - количество уникальных клиентов для рассылок,
        - три случайные статьи из блога.

        :param kwargs:
        :return:
        """
        context = super().get_context_data(**kwargs)
        # количество рассылок всего
        context["mailings_count"] = len(Mailing.objects.all())
        # количество активных рассылок
        context["mailings_count_active"] = len(Mailing.objects.filter(settings__status=True))

        # количество уникальных клиентов для рассылок
        emails_unique = Client.objects.values('email').annotate(total=Count('id'))
        context["emails_unique"] = emails_unique
        context["emails_unique_count"] = len(emails_unique)
        # # три случайные статьи из блога
        # article_list_len = len(Article.objects.all())
        #
        # # article_list_len_2 = Article.objects.Count()
        #
        # context["article_list_len"] = article_list_len
        #
        # valid_profiles_id_list = Article.objects.values_list('id', flat=True)
        # random_profiles_id_list = random.sample(list(valid_profiles_id_list), min(len(valid_profiles_id_list), 3))
        # # context["random_articles"] = Article.objects.filter(id__in=random_profiles_id_list)
        # # = get_cached_article_list()
        # context["random_articles"] = get_cached_article_list().filter(id__in=random_profiles_id_list)
        #
        # # def sample(self, population, k, *, counts=None):

        return context
