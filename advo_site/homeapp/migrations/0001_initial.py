# Generated by Django 4.2 on 2023-07-12 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=12)),
                ('status', models.CharField(choices=[('ДА', 'ПЕРЕЗВОНИЛИ'), ('НЕТ', 'НЕ ПЕРЕЗВОНИЛИ')], default='НЕТ', max_length=3)),
                ('date_application', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_application'],
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100, verbose_name='ФИО')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('want_to', models.CharField(choices=[('option', '-- выбрать --'), ('option_1', 'Прохождение практики'), ('option_2', 'Стажировка'), ('option_3', 'Помощник юриста'), ('option_4', 'Юрист'), ('option_5', 'Адвокат')], default='option', max_length=20, verbose_name='Желаемая позиция')),
                ('education', models.CharField(max_length=100, verbose_name='Место учёбы')),
                ('experience', models.CharField(blank=True, max_length=255, verbose_name='Опыт работы')),
                ('mail', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('covering', models.TextField(blank=True, default=None, verbose_name='Сопроводительное письмо')),
                ('resume', models.FileField(blank=True, upload_to='resume/', verbose_name='Резюме')),
                ('agree', models.BooleanField(verbose_name='Согласие с политикой')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата подачи резюме')),
                ('status', models.CharField(choices=[('ДА', 'Просмотрено'), ('НЕТ', 'Не просмотрено')], default='НЕТ', max_length=3, verbose_name='Статус')),
            ],
            options={
                'verbose_name_plural': 'Резюме',
                'ordering': ['-date'],
            },
        ),
    ]
