from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    ACCESS_LEVEL_CHOICES = (
        ('admin', 'Full access'),
        ('moscow', 'Head office: Moscow'),
        ('ulyanonsk', 'Ulyanovsk branch'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_level = models.CharField(
        max_length=32,
        verbose_name="Место деятельности",
        choices=ACCESS_LEVEL_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"manager - {self.user.username}"

    class Meta:
        verbose_name = "Менеджера"
        verbose_name_plural = "Менеджеры"
