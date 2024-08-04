from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from mailing.models import Mailing


class HomePageView(TemplateView):
    template_name = "mailing/home_page.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = "Главная страница"
        return context_data


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
    fields = ['title', 'description']
    success_url = reverse_lazy("mailing:mailing_list")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ['title', 'description']
    success_url = reverse_lazy("mailing:mailing_list")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy("mailing:mailing_list")


