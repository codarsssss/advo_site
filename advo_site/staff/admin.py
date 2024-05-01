from django.contrib import admin
from django.contrib.auth.models import User
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_user_email', 'access_level')

    def get_username(self, obj):
        return obj.user.username

    def get_user_email(self, obj):
        return obj.user.email
    
    get_user_email.short_description = 'Email'
    get_username.short_description = 'username'


admin.site.register(Employee, EmployeeAdmin)
