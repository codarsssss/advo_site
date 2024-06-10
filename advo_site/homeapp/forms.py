from django import forms
from tinymce.widgets import TinyMCE

from .models import Consultation, Worker, News, Partner


class ConsultationForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label='Имя')
    number = forms.CharField(max_length=12, label='Телефон')
    question = forms.CharField(widget=forms.Textarea, required=False, label='Ваш вопрос (необязательно)')

    class Meta:
        model = Consultation
        fields = ['username', 'number', 'question']


class WorkerForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = ['fio', 'birthday', 'want_to', 'education', 'experience',
                  'mail', 'covering', 'agree', 'resume']


class NewsForm(forms.ModelForm):
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))
    class Meta:
        model = News
        fields = '__all__'


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['name', 'work_place', 'min_context1', 'min_context2', 'min_context3', 'min_context4', 'context', 'photo']
