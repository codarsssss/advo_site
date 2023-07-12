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
        DEFAULT = 'option', '-- выбрать --'
        PRACTICE = 'option_1','Прохождение практики'
        TRAINY = 'option_2', 'Стажировка'
        JURIST_HELPER = 'option_3', 'Помощник юриста'
        JURIST = 'option_4', 'Юрист'
        LAWER = 'option_5', 'Адвокат'

    class StatusView(models.TextChoices):
        CALLED_BACK = 'ДА', 'Просмотрено'
        NO_CALLED_BACK = 'НЕТ', 'Не просмотрено'

    fio = models.CharField(max_length=100, verbose_name='ФИО')
    birthday = models.DateField(verbose_name='Дата рождения')
    want_to = models.CharField(max_length=20,
                               choices=Status.choices,
                               default=Status.DEFAULT,
                               verbose_name='Желаемая позиция')
    education = models.CharField(max_length=100,
                                 verbose_name='Место учёбы')
    experience = models.CharField(blank=True, max_length=255,
                                  verbose_name='Опыт работы')
    mail = models.EmailField(verbose_name='Электронная почта')
    covering = models.TextField(blank=True,
                                default=None,
                                verbose_name='Сопроводительное письмо')

    resume = models.FileField(blank=True, upload_to='resume/',
                              verbose_name='Резюме')

    agree = models.BooleanField(verbose_name='Согласие с политикой')

    date = models.DateTimeField(auto_now_add=True,
                                verbose_name='Дата подачи резюме')
    status = models.CharField(max_length=3,
                              choices=StatusView.choices,
                              default=StatusView.NO_CALLED_BACK,
                              verbose_name='Статус')

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Резюме"

    def str(self):
        return self.fio
