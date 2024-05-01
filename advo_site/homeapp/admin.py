from django.contrib.auth.models import User, Group
from django.contrib import admin
from .forms import NewsForm, PartnerForm
from .models import Consultation, Worker, News, Partner
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


class NewsAdmin(admin.ModelAdmin):
    form = NewsForm
    list_display = ['title', 'slug', 'create_datetime', 'status']
    # Этот атрибут нужен для того, чтобы поле slug создавалось
    # автоматически. Работает только в админке!!!
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['status', 'create_datetime']
    search_fields = ['title', 'slug', 'text']
    ordering = ['status', '-create_datetime']
    readonly_fields = ['create_datetime']


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    form = PartnerForm
    list_display = ['name',]


# admin.site.unregister(User)
# admin.site.unregister(Group)
admin.site.register(News, NewsAdmin)
