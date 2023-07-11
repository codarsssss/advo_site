from django import forms
from .models import Consultation, Worker


class ConsultationForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    number = forms.CharField(max_length=12)

    class Meta:
        model = Consultation
        fields = ['username', 'number']


class WorkerForm(forms.ModelForm):
    Choices = (('не выбран', '0'), ('практика', '1'), ('стажер', '2'), ('юр.помощник', '3'), ('юрист', '4'), ('адвокат', '5'))
    fio = forms.CharField(max_length=100)
    birthday = forms.DateField()
    want_to = forms.CharField(widget=forms.Select(choices=Choices))
    education = forms.CharField(max_length=100)
    experience = forms.CharField()
    mail = forms.CharField(max_length=100)
    covering = forms.CharField(widget=forms.Textarea)
    resume = forms.FileField()
    agree = forms.BooleanField()
    date = forms.DateTimeField()

    class Meta:
        model = Worker
        fields = '__all__'
