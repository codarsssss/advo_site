from django import forms
from tinymce.widgets import TinyMCE

from .models import Consultation, Worker, News


class ConsultationForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    number = forms.CharField(max_length=12)

    class Meta:
        model = Consultation
        fields = ['username', 'number']


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
