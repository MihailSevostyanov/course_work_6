from django.forms import forms, ModelForm, BooleanField, DateField, DateInput

from mailing.models import Client, Mailing, Message, MailingSettings


class StyleFormMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'email', 'comment', 'is_active')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        prohibited_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']
        for word in prohibited_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'Имя не должно содержать слово {word}')
        return cleaned_data


class MailingForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mailing
        fields = ('title', 'description', 'message', 'user', 'settings')

    def clean_title(self):
        cleaned_data = self.cleaned_data['title']
        prohibited_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']
        for word in prohibited_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'Название не должно содержать слово {word}')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        prohibited_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']
        for word in prohibited_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'Описание не должно содержать слово {word}')
        return cleaned_data


class MessageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        fields = ('title', 'body')


class MailingSettingsForm(StyleFormMixin, ModelForm):
    class Meta:
        model = MailingSettings
        fields = ('start_time', 'end_time', 'periodicity', 'status', 'active', 'status_changed')
        created_date = DateField(input_formats=['%d/%m/%Y', ],
                                       widget=DateInput(
                                           attrs={'class': 'datepicker form-control', 'placeholder': 'Select a date'}),
                                       required=False)


class MailingModeratorForm(StyleFormMixin, ModelForm):
    model = Mailing
    fields = ('title', 'description', 'message', 'user', 'settings')
