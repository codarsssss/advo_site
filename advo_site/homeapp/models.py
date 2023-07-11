from django.db import models

# Create your models here.


class Consultation(models.Model):

    class Status(models.TextChoices):
        CALLED_BACK = 'ДА', 'ПЕРЕЗВОНИЛИ'
        NO_CALLED_BACK = 'НЕТ', 'НЕ ПЕРЕЗВОНИЛИ'
    username = models.CharField(max_length=100)
    number = models.CharField(max_length=12)
    status = models.CharField(max_length=3, choices=Status.choices, default=Status.NO_CALLED_BACK)
    date_application = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_application']

    def __str__(self):
        return self.username


class Worker(models.Model):

    class Status(models.TextChoices):
        DEFAULT = 'не выбран', 'не выбран'
        PRACTICE = 'практика','прохождение практики'
        TRAINY = 'стажер', 'стажировка'
        JURIST_HELPER = 'юр.помощник', 'помощник юриста'
        JURIST = 'юрист', 'юрист'
        LAWER = 'адвокат', 'адвокат'

    class StatusView(models.TextChoices):
        CALLED_BACK = 'ДА', 'ПЕРЕЗВОНИЛИ'
        NO_CALLED_BACK = 'НЕТ', 'НЕ ПЕРЕЗВОНИЛИ'
    fio = models.CharField(max_length=100)
    birthday = models.DateField()
    want_to = models.CharField(max_length=20, choices=Status.choices, default=Status.DEFAULT)
    education = models.CharField(max_length=100)
    experience = models.CharField(blank=True, max_length=255)
    mail = models.CharField(max_length=100)
    covering = models.TextField(blank=True)
    resume = models.FileField(blank=True)
    agree = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=3, choices=StatusView.choices, default=StatusView.NO_CALLED_BACK)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.fio




