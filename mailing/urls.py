from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView, \
    HomePageView

app_name = MailingConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('mailing/', MailingListView.as_view(), name='mailing_list'),
    path('mailing/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/detail/<int:pk>', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/update/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/delete/<int:pk>', MailingDeleteView.as_view(), name='mailing_delete'),
]