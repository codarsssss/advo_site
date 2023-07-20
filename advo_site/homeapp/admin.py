from django.contrib import admin
from .models import Consultation, Worker
from django.urls import reverse
from django.utils.html import format_html


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ['username', 'number', 'date_application', 'status']
    list_filter = ['status', 'date_application', 'username']
    search_fields = ['username', 'number', 'date_application']
    ordering = ['status', 'date_application', 'username']
    readonly_fields = ['username', 'number']


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['fio', 'want_to', 'mail', 'status']
    list_filter = ['fio', 'want_to', 'status']
    search_fields = ['fio', 'want_to', 'date', 'status']
    readonly_fields = ['fio', 'want_to', 'mail', 'download_resume']
    exclude = ('resume',)

    def download_resume(self, obj):
        if obj.resume:
            url = reverse('homeapp:download', kwargs={'file_path': obj.resume.name})
            return format_html('<a href="{}">Скачать</a>', url)
        return '-'

    download_resume.short_description = 'Резюме'
