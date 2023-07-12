from django import forms
from .models import Consultation, Worker


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
