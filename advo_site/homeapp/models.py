from django.db import models
from django.db.models.query import QuerySet
from transliterate import slugify
from django.utils.safestring import mark_safe
from django.urls import reverse


def translit_filename(instance, filename):
    file_extension = filename.split(".")[-1]
    filename = slugify(instance.fio)
    return "resume/{}.{}".format(filename, file_extension)


class Consultation(models.Model):
    class Status(models.TextChoices):
        CALLED_BACK = "ДА", "ПЕРЕЗВОНИЛИ"
        NO_CALLED_BACK = "НЕТ", "НЕ ПЕРЕЗВОНИЛИ"

    username = models.CharField(max_length=100, verbose_name="Имя")
    number = models.CharField(max_length=12, verbose_name="Телефон")
    question = models.TextField(blank=True, null=True, verbose_name="Ваш вопрос (необязательно)")
    status = models.CharField(
        max_length=3, choices=Status.choices, default=Status.NO_CALLED_BACK, verbose_name="Статус"
    )
    date_application = models.DateTimeField(auto_now_add=True, verbose_name="Дата заявки")

    class Meta:
        ordering = ["-date_application"]
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"{self.username}"


class Worker(models.Model):
    class Status(models.TextChoices):
        DEFAULT = "option", "-- выбрать --"
        PRACTICE = "option_1", "Прохождение практики"
        TRAINY = "option_2", "Стажировка"
        JURIST_HELPER = "option_3", "Помощник юриста"
        JURIST = "option_4", "Юрист"
        LAWER = "option_5", "Адвокат"

    class StatusView(models.TextChoices):
        CALLED_BACK = "ДА", "Просмотрено"
        NO_CALLED_BACK = "НЕТ", "Не просмотрено"

    fio = models.CharField(max_length=100, verbose_name="ФИО")
    birthday = models.DateField(verbose_name="Дата рождения")
    want_to = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DEFAULT,
        verbose_name="Желаемая позиция",
    )
    education = models.CharField(max_length=100, verbose_name="Место учёбы")
    experience = models.CharField(
        blank=True, max_length=255, verbose_name="Опыт работы"
    )
    mail = models.EmailField(verbose_name="Электронная почта")
    covering = models.TextField(
        blank=True, default=None, verbose_name="Сопроводительное письмо"
    )

    resume = models.FileField(
        blank=True, upload_to=translit_filename, verbose_name="Резюме"
    )

    agree = models.BooleanField(verbose_name="Согласие с политикой")

    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата подачи резюме")
    status = models.CharField(
        max_length=3,
        choices=StatusView.choices,
        default=StatusView.NO_CALLED_BACK,
        verbose_name="Статус",
    )

    class Meta:
        ordering = ["-date"]
        verbose_name_plural = "Резюме"

    def str(self):
        return self.fio


class NewsPublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status=News.Status.PUBLISHED)


# Модель новостей
class News(models.Model):
    class Status(models.TextChoices):
        NOT_PUBLISHED = "Нет", "Не опубликована"
        PUBLISHED = "Да", "Опубликована"

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(verbose_name="Слаг поста")
    text = models.TextField(verbose_name="Текст новости")
    status = models.CharField(
        verbose_name="Статус",
        max_length=3,
        choices=Status.choices,
        default=Status.NOT_PUBLISHED,
    )
    create_datetime = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )

    objects = models.Manager()  # Менеджер, применяемый по умолчанию
    published = NewsPublishedManager()  # Конкретно-прикладной менеджер

    class Meta:
        ordering = ["-create_datetime"]

        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title


class Partner(models.Model):
    WORK_PLACE_CHOICES = (
        ('moscow', 'Head office: Moscow'),
        ('ulyanovsk', 'Ulyanovsk branch')
    )

    name = models.CharField(max_length=50, verbose_name="Фамилия Имя Отчество")
    work_place = models.CharField(
        max_length=32,
        verbose_name="Место деятельности",
        choices=WORK_PLACE_CHOICES, 
        default="moscow",
        blank=True,
        null=True
    )
    min_context1 = models.TextField(verbose_name="Краткое описание для первой страницы")
    min_context2 = models.TextField(
        blank=True, verbose_name="Дополнительное поле короткого писания"
    )
    min_context3 = models.TextField(
        blank=True, verbose_name="Дополнительное поле короткого писания"
    )
    min_context4 = models.TextField(
        blank=True, verbose_name="Дополнительное поле короткого писания"
    )
    context = models.TextField(verbose_name="Полное описание")
    photo = models.ImageField(verbose_name="Фото", upload_to="partners/")
    time_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-time_create"]

        verbose_name = "Партнера"
        verbose_name_plural = "Партнеры"

    def __str__(self):        
        return f"{self.name}: {self.work_place}"


class PracticeCategory(models.Model):
    title = models.CharField(
        max_length=128, verbose_name="Наименование категории практики"
        )
    image = models.ImageField(
        verbose_name="Изображение", upload_to="practice_category/", blank=True, null=True
        )
    class Meta:
        verbose_name = "Категорию практики"
        verbose_name_plural = "Категории практик"

    def __str__(self):        
        return f"{self.title}"

class PracticeInstance(models.Model):
    WORK_PLACE_CHOICES = (
        ('moscow', 'Head office: Moscow'),
        ('ulyanovsk', 'Ulyanovsk branch')
    )

    work_place = models.CharField(
        max_length=32,
        verbose_name="Принадлежность случая",
        choices=WORK_PLACE_CHOICES, 
        default="moscow",
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        PracticeCategory,
        on_delete=models.CASCADE,
        verbose_name="Категория практики"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название случая"
        )
    circumstances = models.TextField(
        verbose_name="Обстоятельства"
    )
    lawyer_position = models.TextField(
        verbose_name="Позиция адвоката"
    )
    outcome = models.TextField(
        verbose_name="Итог"
    )

    verdict_url = models.URLField(
        verbose_name="Ссылка на приговор",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Случай практики"
        verbose_name_plural = "Случаи практики"

    def __str__(self):
        return f"{self.title}"


class PracticeInstanceImage(models.Model):
    practice_instance = models.ForeignKey(
        PracticeInstance,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name="Случай практики"
    )
    image = models.ImageField(
        upload_to='practice_instance_images/',
        verbose_name="Изображение"
    )

    class Meta:
        verbose_name = "Изображение случая практики"
        verbose_name_plural = "Изображения случаев практики"

    def __str__(self):
        return f"Image for {self.practice_instance}"
