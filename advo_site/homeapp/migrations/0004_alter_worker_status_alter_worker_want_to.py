# Generated by Django 4.2 on 2023-07-11 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0003_worker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='status',
            field=models.CharField(choices=[('ДА', 'ПЕРЕЗВОНИЛИ'), ('НЕТ', 'НЕ ПЕРЕЗВОНИЛИ')], default='НЕТ', max_length=3),
        ),
        migrations.AlterField(
            model_name='worker',
            name='want_to',
            field=models.CharField(choices=[('не выбран', 'не выбран'), ('практика', 'прохождение практики'), ('стажер', 'стажировка'), ('юр.помощник', 'помощник юриста'), ('юрист', 'юрист'), ('адвокат', 'адвокат')], default='не выбран', max_length=20),
        ),
    ]
