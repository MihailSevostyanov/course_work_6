from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView, \
    HomePageView, ClientListView, ClientCreateView, ClientDetailView, ClientUpdateView, ClientDeleteView, \
    MessageListView, MessageCreateView, MessageUpdateView, MessageDeleteView, MailingSettingsListView, \
    MailingSettingsCreateView, MailingSettingsUpdateView, MailingSettingsDeleteView, MailingSettingsDetailView, \
    MessageDetailView

app_name = MailingConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('mailing/', MailingListView.as_view(), name='mailing_list'),
    path('mailing/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/detail/<int:pk>', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/update/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/delete/<int:pk>', MailingDeleteView.as_view(), name='mailing_delete'),

    path('mailing/message/', MessageListView.as_view(), name='message_list'),
    path('mailing/message/create/', MessageCreateView.as_view(), name='message_create'),
    path('mailing/message/detail/<int:pk>', MessageDetailView.as_view(), name='message_detail'),
    path('mailing/message/update/<int:pk>', MessageUpdateView.as_view(), name='message_update'),
    path('mailing/message/delete/<int:pk>', MessageDeleteView.as_view(), name='message_delete'),

    path('mailing/settings/', MailingSettingsListView.as_view(), name='settings_list'),
    path('mailing/settings/create/', MailingSettingsCreateView.as_view(), name='settings_create'),
    path('mailing/settings/detail/<int:pk>', MailingSettingsDetailView.as_view(), name='settings_detail'),
    path('mailing/settings/update/<int:pk>', MailingSettingsUpdateView.as_view(), name='settings_update'),
    path('mailing/settings/delete/<int:pk>', MailingSettingsDeleteView.as_view(), name='settings_delete'),

    path('mailing/client/', ClientListView.as_view(), name='client_list'),
    path('mailing/client/create/', ClientCreateView.as_view(), name='client_create'),
    path('mailing/client/detail/<int:pk>', ClientDetailView.as_view(), name='client_detail'),
    path('mailing/client/update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('mailing/client/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),
]
