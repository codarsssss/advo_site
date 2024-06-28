from django.contrib.auth.models import User, Group
from django.contrib import admin
from .forms import NewsForm, PartnerForm
from .models import Consultation, Worker, News, Partner
from django.urls import reverse
from django.utils.html import format_html
from .models import PracticeCategory, PracticeInstance, PracticeInstanceImage


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ['username', 'number', 'date_application', 'status']
    list_filter = ['status', 'date_application', 'username']
    search_fields = ['username', 'number', 'date_application']
    ordering = ['status', 'date_application', 'username']
    readonly_fields = ['username', 'number', 'date_application']
    
    fieldsets = (
        (None, {
            'fields': ('date_application', 'username', 'number', 'status', )
        }),
        ('Вопрос клиента', {
            'fields': ('question', ),
            'classes': ('collapse',) 
        }),
    )


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


class PracticeCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)

class PracticeInstanceImageInline(admin.TabularInline):
    model = PracticeInstanceImage
    extra = 1  # Количество пустых форм для новых изображений

class PracticeInstanceAdmin(admin.ModelAdmin):
    list_display = ('title', 'work_place', 'get_category_title')
    search_fields = ('title', 'circumstances', 'lawyer_position', 'outcome')
    list_filter = ('work_place', 'category__title')
    list_editable = ('work_place',)
    fieldsets = (
        (None, {
            'fields': ('title', 'work_place', 'category')
        }),
        ('Details', {
            'fields': ('circumstances', 'lawyer_position', 'outcome')
        }),
    )
    inlines = [PracticeInstanceImageInline]

    def get_category_title(self, obj):
        return obj.category.title
    get_category_title.short_description = 'Category Title'
    get_category_title.admin_order_field = 'category__title'

class PracticeInstanceImageAdmin(admin.ModelAdmin):
    list_display = ('practice_instance', 'image')
    search_fields = ('practice_instance__title',)
    list_filter = ('practice_instance',)

# Register models with admin site
admin.site.register(PracticeCategory, PracticeCategoryAdmin)
admin.site.register(PracticeInstance, PracticeInstanceAdmin)
admin.site.register(PracticeInstanceImage, PracticeInstanceImageAdmin)

# admin.site.unregister(User)
# admin.site.unregister(Group)
admin.site.register(News, NewsAdmin)
